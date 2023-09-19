<template>
  <el-row>

    <el-card :body-style="{ padding: '10px' }"  style="height: 80%;width:100%;display:inline-block;gutter:0;">
      <h3 style="background-color: #f5f5f5; padding: 5px 10px; border-radius: 4px;margin-top: 0; margin-bottom: 0; ">Story</h3>
      <el-progress
          :percentage="progress.style"
          stroke-linecap="butt"
          type="line"
          :stroke-width="2"
          color="#bdbdbd"
          :show-text="false"
          style="margin-top: 0; margin-bottom: 10px;"
      ></el-progress>
      <el-form label-width="0px" class="form">
        <el-form-item>
          <el-input
              type="textarea"
              :rows="12"
              placeholder="Input your story here."
              v-model="textarea">
          </el-input>
        </el-form-item>


        <el-row :gutter="20">

          <el-col :span="12" >
            <el-form-item>
              <el-input-number v-model="value" @change="handleNumChange" :min="1" :max="6" size="small"></el-input-number>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item>
              <div class="button-group">
                <!--<el-button @click="handleStyle" size="small">Generate Style</el-button>
                <el-button @click="drawer = true" size="small">Edit Style</el-button>-->
                <el-button @click="handleAllGenerate" size="small">Submit</el-button>
                <el-button icon="el-icon-setting" circle @click="drawer = true"></el-button>

              </div>
            </el-form-item>
          </el-col>
        </el-row>

      </el-form>
    </el-card>
    <el-card :body-style="{ padding: '10px' }" style="height: 80%;width:100%;display:inline-block;gutter:0">
      <h3 style="background-color: #f5f5f5; padding: 10px 10px; border-radius: 4px;margin-top: 0;margin-bottom: 0;">Style</h3>
      <el-progress
          :percentage="progress.submit"
          stroke-linecap="butt"
          type="line"
          :stroke-width="2" color="#bdbdbd"
          :show-text="false"
          style="margin-top: 0; margin-bottom: 10px;"
      ></el-progress>
      <el-form label-width="0px" class="form">
        <el-form :model="promptForm" ref="promptForm" label-width="60px" > <!-- 在这里添加了边框样式style=" padding: 6px;"  -->
<!--          <h3 style="padding: 0px 10px; margin-top: 0;">Character Settings</h3>-->
          <el-row :gutter="20"> <!-- 使内容在一行内显示两个 -->
            <el-col :span="12">
              <el-form-item class="custom-label-size" size="mini" label="Age" prop="character.age">
                <el-input v-model="promptForm.character.age" size="mini" style="width: 90%"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item size="mini" label="Gender" prop="character.gender">
                <el-input v-model="promptForm.character.gender" size="mini" style="width: 90%"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item size="mini" label="Hair" prop="character.hair">
                <el-input v-model="promptForm.character.hair" size="mini" style="width: 90%"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item size="mini" label="Clothing" prop="character.clothing">
                <el-input v-model="promptForm.character.clothing" size="mini" style="width: 90%"></el-input>
              </el-form-item>
            </el-col>
          </el-row>
<!--          <h3 style="padding: 0px 10px; margin-top: 0;" >Background</h3>-->
          <el-form-item size="mini" label="Scene" prop="background.scene">
            <el-input v-model="promptForm.background.scene"
                      size="mini" style="width: 95%"></el-input>
          </el-form-item>
          <el-form-item size="mini" label="Location" prop="background.location">
            <el-input  v-model="promptForm.background.location"
                      size="mini" style="width: 95%"></el-input><!--:autosize="{ minRows: 2, maxRows: 4}"-->
          </el-form-item>
<!--          <h3 style="padding: 0px 10px; margin-top: 0;">Artistic Style</h3>-->
          <el-form-item size="mini" label="Color" prop="style.color">
            <el-input v-model="promptForm.style.color" size="mini" style="width: 95%"></el-input>
          </el-form-item>
          <el-form-item size="mini" label="ArtType" prop="style.artType">
            <el-input v-model="promptForm.style.artType"
                      size="mini" style="width: 95%"></el-input>
          </el-form-item>
          <el-form-item size="mini" label="Lens" prop="style.lens">
            <el-input v-model="promptForm.style.lens" size="mini" style="width: 95%"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button @click="handleStyle" size="small">Regenerate style</el-button>
            <el-button size="small" @click="submitForm('promptForm')">Resubmit</el-button>
            <el-button size="small" @click="resetForm('promptForm')">Reset</el-button>
          </el-form-item>
        </el-form>
        <el-drawer
            title="Edit Prompt"
            :visible.sync="drawer"
            :with-header="false"
            size="30%"
            direction="ltr">
          <el-tabs type="border-card" style="height: 100%;width:100%;display:inline-block;gutter:3">
            <!--<el-tab-pane>
              <span slot="label" style="color: black; font-size: 12px"><i class="el-icon-s-help"></i>  Style</span>
              <el-form :model="promptForm" ref="promptForm" label-width="100px">
                <h3>Character Settings</h3>
                <el-form-item label="Age" prop="character.age">
                  <el-input v-model="promptForm.character.age" style="width: 90%"></el-input>
                </el-form-item>
                <el-form-item label="Gender" prop="character.gender" >
                  <el-input v-model="promptForm.character.gender" style="width: 90%"></el-input>
                </el-form-item>
                <el-form-item label="Hair" prop="character.hair">
                  <el-input v-model="promptForm.character.hair" style="width: 90%"></el-input>
                </el-form-item>
                <el-form-item label="Clothing" prop="character.clothing">
                  <el-input v-model="promptForm.character.clothing" style="width: 90%"></el-input>
                </el-form-item>
                <h3>Background</h3>
                <el-form-item label="Scene" prop="background.scene">
                  <el-input v-model="promptForm.background.scene" type="textarea"
                            :autosize="{ minRows: 2, maxRows: 4}" style="width: 90%"></el-input>
                </el-form-item>
                <el-form-item label="Location" prop="background.location">
                  <el-input v-model="promptForm.background.location" type="textarea"
                            :autosize="{ minRows: 2, maxRows: 4}" style="width: 90%"></el-input>
                </el-form-item>
                <h3>Artistic Style</h3>
                <el-form-item label="Color" prop="style.color">
                  <el-input v-model="promptForm.style.color" style="width: 90%"></el-input>
                </el-form-item>
                <el-form-item label="Art Type" prop="style.artType">
                  <el-input v-model="promptForm.style.artType" type="textarea"
                            :autosize="{ minRows: 2, maxRows: 4}" style="width: 90%"></el-input>
                </el-form-item>
                <el-form-item label="lens" prop="style.lens">
                  <el-input v-model="promptForm.style.lens" style="width: 90%"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button @click="handleStyle" size="small">Regenerate style</el-button>
                  <el-button type="primary" size="small" @click="submitForm('promptForm')">Submit</el-button>
                  <el-button size="small" @click="resetForm('promptForm')">Reset</el-button>
                </el-form-item>
              </el-form>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label" style="color: black; font-size: 12px"><i class="el-icon-cpu"></i>  GPT4</span>
              <span slot="default" style="color: black; font-size: 12px">
                GPT-4 is a large-scale multimodal model that can take both image and text inputs and generate text as output. It achieves human-level performance in various professional and academic benchmark tests.
              </span>
            </el-tab-pane>-->
            <el-tab-pane>
              <span slot="label" style="color: black; font-size: 12px"><i class="el-icon-cpu"></i> Style Prompt</span>
              <el-input type="textarea" v-model="stylePrompt" :rows="30" />
              <el-button @click="saveStyle">Save</el-button>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label" style="color: black; font-size: 12px"><i class="el-icon-document"></i> Transfer Prompt</span>
              <el-input type="textarea" v-model="transferPrompt" :rows="30" />
              <el-button @click="saveTransfer">Save</el-button>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label" style="color: black; font-size: 12px"><i class="el-icon-more"></i> Select Model</span>
              <el-select v-model="selectedOption" @change="handleSelectionChange">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
              </el-select>
              <div v-if="isLoading">Loading, please wait...</div>
            </el-tab-pane>

          </el-tabs>

        </el-drawer>
      </el-form>


    </el-card>

  </el-row>

</template>

<script>
import axios from 'axios';

export default {
  props: ['progress'],
  data() {
    return {
      selectedOption: 'deliberate_v2.safetensors',
      options: [
        { value: 'AnimalSketch.ckpt [77d8250fbb]', label: 'AnimalSketch' },
        { value: 'AnythingV5_v5PrtRE.safetensors [7f96a1a9ca]', label: 'AnythingV5_v5PrtRE' },
        { value: 'beautifulRealistic_brav5.safetensors', label: 'beautifulRealistic_brav5' },
        { value: 'cyberrealistic_v30.safetensors', label: 'cyberrealistic_v30' },
        { value: 'deliberate_v2.safetensors', label: 'deliberate_v2' },
        { value: 'disneyPixarCartoon_v10.safetensors', label: 'disneyPixarCartoon_v10' },
        { value: 'dynavisionXLAllInOneStylized_alpha036FP16Bakedvae.safetensors [2797fe9939]', label: 'dynavisionXLAllnOneStylized' },//
        { value: 'majicmixRealistic_v5.safetensors', label: 'majicmixRealistic' },
        { value: 'meartsty.ckpt', label: 'meartsty' },
        { value: 'nextphoto_v20.safetensors', label: 'nextphoto_v20.safetensors' },
        { value: 'queratograySketch_v10.safetensors', label: 'queratograySketch_v10' },
        { value: 'samaritan3dCartoon_v10.safetensors', label: 'samaritan3dCartoon_v10' },
        { value: 'sd_xl_base_1.0.safetensors [31e35c80fc]', label: 'sd_xl_base_1.0' },
        { value: 'v1-5-pruned-emaonly.safetensors [6ce0161689]', label: 'v1-5-pruned-emaonly' },
        { value: 'v2-1_768-ema-pruned.ckpt', label: 'v2-1_768-ema-pruned' },
        { value: 'xsarchitecturalv3com_v31.ckpt', label: 'xsarchitecturalv3com' },
        { value: 'realisticVisionV51_v51VAE.safetensors', label: 'realisticVisionV51_v51VAE' },
      ],
      isLoading: false,
      stylePrompt: '',
      transferPrompt: '',
      originalStylePrompt: '',
      editedStylePrompt: '',
      textarea: '',
      value: 6,
      //selectedOption: '',
      drawer: false,
      style:'',
      storycontent:'',
      promptForm: {  // Define promptForm here
        character: {
          age: '',
          gender: '',
          hair: '',
          clothing: ''
        },
        background: {
          scene: '',
          location: ''
        },
        style: {
          color: '',
          artType: '',
          lens:''
        }
      }
    }
  },
  async mounted() {
    try {
      await axios.get(`${this.$apiUrl}:5010/api/resetTempFiles`);
      await this.fetchStyle();
      await this.fetchTransfer();
    } catch (error) {
      console.error("Error in mounted lifecycle hook:", error);
    }
  },

  methods: {

    handleSelectionChange(value) {
      this.$emit('selected-option', value); // 将选中的值传递给父组件
      this.isLoading = true;

      // 延迟 10 秒
      setTimeout(() => {
        this.isLoading = false;
      }, 15000);
    },
    async fetchStyle() {
      try {
        const response = await axios.get(`${this.$apiUrl}:5010/api/fetchStyle`);
        this.stylePrompt = response.data.content;
      } catch (error) {
        console.error("Error fetching style:", error);
      }
    },
    async fetchTransfer() {
      try {
        const response = await axios.get(`${this.$apiUrl}:5010/api/fetchTransfer`);
        this.transferPrompt = response.data.content;
      } catch (error) {
        console.error("Error fetching transfer:", error);
      }
    },
    async saveStyle() {
      try {
        await axios.post(`${this.$apiUrl}:5010/api/saveStyle`, { content: this.stylePrompt });
      } catch (error) {
        console.error("Error saving style:", error);
      }
    },
    async saveTransfer() {
      try {
        await axios.post(`${this.$apiUrl}:5010/api/saveTransfer`, { content: this.transferPrompt });
      } catch (error) {
        console.error("Error saving transfer:", error);
      }
    },


    submitForm(formName) {
      this.syncStyleWithPromptForm();
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
          await this.handleStory();
          await this.handleSubmit(); // 提交内容
          this.$emit('startAllGenerate');// Submit the form
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    handleNumChange() {
      this.$emit('change', this.value);
    },
    async handleStyle() {
      this.$emit('taskStart', 'style');
      console.log(this.textarea); // 打印输入的内容

      try {
        const response = await axios.post(`${this.$apiUrl}:5000/api/style`, {
          content: this.textarea,
          model: 'gpt-4',
          temperature: 1,
        });

        const style = response.data.content;
        this.style = style;// Change variable name here
        console.log(style);
        this.$saveLogToServer('Style:');
        this.$saveLogToServer(style);
        // Extract the content within the curly braces and assign them to the corresponding properties
        const ageMatch = style.match(/Age:\{(.*?)\}/);
        if (ageMatch) this.promptForm.character.age = ageMatch[1];

        const genderMatch = style.match(/Gender:\{(.*?)\}/);
        if (genderMatch) this.promptForm.character.gender = genderMatch[1];

        const hairMatch = style.match(/Hair:\{(.*?)\}/);
        if (hairMatch) this.promptForm.character.hair = hairMatch[1];

        const clothingMatch = style.match(/Clothing:\{(.*?)\}/);
        if (clothingMatch) this.promptForm.character.clothing = clothingMatch[1];

        const sceneMatch = style.match(/Scene:\{(.*?)\}/);
        if (sceneMatch) this.promptForm.background.scene = sceneMatch[1];

        const locationMatch = style.match(/location:\{(.*?)\}/);
        if (locationMatch) this.promptForm.background.location = locationMatch[1];

        const colorMatch = style.match(/Color:\{(.*?)\}/);
        if (colorMatch) this.promptForm.style.color = colorMatch[1];

        const artTypeMatch = style.match(/Art_type:\{(.*?)\}/);
        if (artTypeMatch) this.promptForm.style.artType = artTypeMatch[1];

        const lensMatch = style.match(/Lens&Shot:\{(.*?)\}/);
        if (artTypeMatch) this.promptForm.style.lens = lensMatch[1];

        console.log(this.promptForm);
        this.$emit('taskComplete', 'style');
      } catch (error) {
        console.error(error);
      }
    },
    syncStyleWithPromptForm() {
      this.style = `Age:{${this.promptForm.character.age}},Gender:{${this.promptForm.character.gender}},Hair:{${this.promptForm.character.hair}},Clothing:{${this.promptForm.character.clothing}},Scene:{${this.promptForm.background.scene}},Location:{${this.promptForm.background.location}},Color:{${this.promptForm.style.color}},Art_type:{${this.promptForm.style.artType}},Lens&Shot:{${this.promptForm.style.lens}}`; // 使用trim()移除字符串两端的空格
    },
    async handleAllGenerate() {
      await this.handleStyle();
      await this.handleStory();
      await this.handleSubmit(); // 提交内容
      this.$emit('startAllGenerate');
    },


    async handleStory() {
      this.$emit('taskStart', 'submit');
      //console.log(this.textarea); // 打印输入的内容
      //console.log(this.selectedOption); // 打印选中的选项

      console.log(this.value); // 打印 value

      try {
        const combinedContent = this.textarea //+" // " + this.style;//this.style + "//" + this.textarea //
        this.$saveLogToServer('User input');
        this.$saveLogToServer(combinedContent);
        console.log(combinedContent)
        const response = await axios.post(`${this.$apiUrl}:5001/api/generate_story`, {
          content: combinedContent,
          model: 'gpt-4',
          temperature: 1,
          value: this.value  // 添加这一行
        });

        // 提取代码单元格
        const content = response.data.content;
        console.log(content);
        this.storycontent = content;
        // const prompts = content.trim().split(/\n{2,}/)  // 使用两个或更多的换行符来分割提示
        //     .map(prompt => prompt.replace(/'Prompt \d+'\n/, ''));  // 使用正则表达式去除 'Prompt X' 这样的编号
        // console.log(prompts);
        const stores = content.trim().split(/\n{2,}/)  // 使用两个或更多的换行符来分割提示
            .map(story => {
              // 使用正则表达式去除 'Prompt X' 或 'Prompt X : Some description' 这样的模式
              story = story.replace(/'Prompt \d+( : .+)?'\n/, '');
              // 使用正则表达式去除 ```vbnet
              story = story.replace(/^```vbnet\n/, '')
              const lines = story.split('\n');
              // 如果有回车，则仅保留回车之后的内容
              if (lines.length > 1) {
                return lines.slice(1).join('\n');
              }
              return story;
            });
        this.$saveLogToServer(stores);
        console.log(stores);

        // 触发 submit 事件并传递 prompts
        this.$emit('submitStory', stores);
        this.$emit('taskComplete', 'submit');
      } catch (error) {
        console.error(error);
      }
    },


    async handleSubmit() {
      this.$emit('taskStart', 'submit');
      //console.log(this.textarea); // 打印输入的内容
      //console.log(this.selectedOption); // 打印选中的选项
      console.log(this.value); // 打印 value

      try {
        const combinedContent = this.storycontent +" // " + this.style;//this.style + "//" + this.textarea //
        this.$saveLogToServer('story + style');
        this.$saveLogToServer(combinedContent);
        console.log(combinedContent)
        const response = await axios.post(`${this.$apiUrl}:5001/api/generate_prompt`, {
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
        console.log(prompts);

        // 触发 submit 事件并传递 prompts
        this.$emit('submit', prompts);
        this.$emit('taskComplete', 'submit');
      } catch (error) {
        console.error(error);
      }
    }


  }
}
</script>
<style scoped>
.button-group {
  display: inline-flex;
  min-width: 350px;  /* Adjust this value based on your button widths and gaps */
}

.form, .form .el-form-item__label, .form .el-form-item__content {
  font-size: 12px !important;
}
.custom-label-size .el-form-item__label {
  font-size: 12px; /* 你可以根据需要修改这个值 */
}

.extra-margin {
  margin-right: 20px !important;
}
</style>

