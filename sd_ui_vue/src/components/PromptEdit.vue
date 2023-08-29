<template>
  <div class="card">
    <el-row>
      <el-col style="position: relative;">
        <!-- 根据showPrompt的值来决定显示哪一个el-input -->
        <div class="flip-container" :class="{ flipped: showPrompt }">
          <div class="flipper">
            <div class="front">
              <el-input type="textarea" class="prompt-text" v-model="localStory" rows="6"></el-input>
            </div>
            <div class="back">
              <el-input type="textarea" class="prompt-text" v-model="localPrompt" rows="6"></el-input>
            </div>
          </div>
        </div>
<!--        <el-input v-if="showPrompt" type="textarea" class="prompt-text" v-model="localPrompt" rows="5"></el-input>-->
<!--        <el-input v-else type="textarea" class="prompt-text" v-model="localStory" rows="5"></el-input>-->

        <!-- 新增的按钮用来在两个el-input之间切换 -->

        <el-button class="toggle-button" @click="toggleInput" icon="el-icon-open"></el-button>
        <el-button v-if="!showPrompt" class="transfer-button" icon="el-icon-refresh" @click="storyToPrompt"></el-button>
        <el-button v-if="showPrompt" class="generate-button" icon="el-icon-caret-right" @click="generateImage"></el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios';
import html2canvas from 'html2canvas'; // Import the html2canvas library

export default {
  props: ['prompt', 'story', 'index', 'selectedModel'],  // 添加 'index'
  data() {
    return {
      showPrompt: false,
      imageUrl: '',
      localPrompt: this.prompt,
      localStory: this.story,
      drawer: false
    }
  },
  watch: {
    prompt(newVal) {
      this.localPrompt = newVal;
      this.showPrompt = true;
    },
    story(newVal) {
      this.localStory = newVal;
    },
    selectedModel: { // 监视 selectedModel
      immediate: true, // 立即执行一次
      handler(newModel) {
        const option_payload = {
          "sd_model_checkpoint": newModel, // 使用新模型
        };

        // 发送请求
        axios.post('http://144.202.103.70:7861/sdapi/v1/options', option_payload)
            .then(response => {
              console.log('Model updated successfully');
            })
            .catch(error => {
              console.error('Failed to update model:', error);
            });
      }
    }
  },
  created() {

    //console.log(this.localPrompt);  // 打印 prompt
  },
  methods: {
    toggleInput() {
      this.showPrompt = !this.showPrompt;  // 切换showPrompt的值
    },
    async storyToPrompt() {
      //this.$emit('taskStart', 'submit');
      //console.log(this.textarea); // 打印输入的内容
      //console.log(this.selectedOption); // 打印选中的选项

      console.log(this.localStory); // 打印 value

      try {
        const combinedContent = this.localStory +" // " + this.style;//this.style + "//" + this.textarea //
        this.$saveLogToServer('story part + style');
        this.$saveLogToServer(combinedContent);
        console.log(combinedContent)
        const response = await axios.post('http://144.202.103.70:5001/api/generate_one_prompt', {
          content: combinedContent,
          model: 'gpt-4',
          temperature: 1,
          value: this.value  // 添加这一行
        });

        // 提取代码单元格
        const content = response.data.content;
        console.log(content);

        // const prompts = content.trim().split(/\n{2,}/)  // 使用两个或更多的换行符来分割提示
        //     .map(prompt => prompt.replace(/'Prompt \d+'\n/, ''));  // 使用正则表达式去除 'Prompt X' 这样的编号
        // console.log(prompts);
        const prompts = content.trim().split(/\n{2,}/)  // 使用两个或更多的换行符来分割提示
            .map(prompt => {
              // 使用正则表达式去除 'Prompt X' 或 'Prompt X : Some description' 这样的模式
              prompt = prompt.replace(/'Prompt \d+( : .+)?'\n/, '');
              // 使用正则表达式去除 ```vbnet
              prompt = prompt.replace(/^```vbnet\n/, '')
              const lines = prompt.split('\n');
              // 如果有回车，则仅保留回车之后的内容
              if (lines.length > 1) {
                return lines.slice(1).join('\n');
              }
              return prompt;
            });
        this.$saveLogToServer('Prompt');
        this.$saveLogToServer(prompts);
        console.log(prompts);
        this.localprompt = prompts;
        // 触发 submit 事件并传递 prompts
        //this.$emit('submit', prompts);
        //this.$emit('taskComplete', 'submit');
      } catch (error) {
        console.error(error);
      }
    },


    async generateImage() {
      this.$emit('taskStart', 'image');
      const payload = {
        "sd_model_checkpoint": this.selectedModel,//"deliberate_v2.safetensors [9aba26abdf]",////"disneyPixarCartoon_v10.safetensors [d6548414b4]",
        "negative_prompt": "((nude) ,(NSFW),deformed, bad anatomy, disfigured, poorly drawn face, mutation, mutated, extra limb, ugly, disgusting, poorly drawn hands, missing limb, floating limbs, disconnected limbs, malformed hands, blurry, ((((mutated hands and fingers)))), watermark, watermarked, oversaturated, censored, distorted hands, amputation, missing hands, obese, doubled face, double hands, b&w",
        "save_images": true,
        prompt: this.localPrompt,
        steps: 20
      };
      console.log(payload)
      try {
        const response = await axios.post('http://144.202.103.70:7861/sdapi/v1/txt2img', payload);
        const images = response.data.images;
        if (images.length > 0) {
          const imageUrl = 'data:image/png;base64,' + images[0];
          this.$emit('imageGenerated', this.index, imageUrl);  // 添加 this.index
          // Generate the image using html2canvas and display it in the hidden <img> element

        }
        this.$emit('taskComplete', 'image');
      } catch (error) {
        console.error(error);
      }
    },

  }
}
</script>

<style scoped>
.flip-container {
  /*perspective: 1000px;*/
  width: 100%; /* 或者你需要的具体宽度 */
  min-height: 120px; /* 根据你的el-input来调整 */
  position: relative;
}

.flipper {
  width: 100%;
  height: 100%;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  position: relative;
}

.front, .back {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  backface-visibility: hidden;
  display: block;
  align-items: center;
  justify-content: center;
}

.front {
  transform: rotateY(0deg);
}

.back {
  transform: rotateY(180deg);
}

.flip-container.flipped .flipper {
  transform: rotateY(180deg);
}

.prompt-text {
  font-size: 8px;
  width: 100%;
}

.toggle-button {
  font-size: 12px;
  padding: 5px 5px;
  position: absolute;
  top: 2px;
//right: 15px;
  left: -2px;
  background: none;
  border: none;
  outline: none;
  cursor: pointer;
}
.transfer-button {
  font-size: 12px;
  padding: 5px 5px;
  position: absolute;
  top: 22px;
//right: 15px;
  left: -12px;
  background: none;
  border: none;
  outline: none;
  cursor: pointer;
}
.generate-button {
  font-size: 12px;
  padding: 5px 5px;
  position: absolute;
  top: 22px;
  //right: 15px;
  left: -12px;
  background: none;
  border: none;
  outline: none;
  cursor: pointer;
}

.card {
  padding: 10px; /* 因为我们移除了el-card，这里可以加上原来的padding */
}

</style>
