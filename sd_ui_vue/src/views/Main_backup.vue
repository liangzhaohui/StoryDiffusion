<template>
  <main>
    <el-row :gutter="3" class="outer">
      <el-col :span="7" class="overall">
        <el-row :gutter="3" style="height: 50%;">
          <el-col :span="24">
            <div class="grid-content bg-purple-light">
              <input-view @change="handleChange" @submit="handleSubmit" @startAllGenerate="handleAllGenerate" @taskStart="startTask" @taskComplete="completeTask" :progress="progress" @selected-option="updateSelectedOption"></input-view>
            </div>
          </el-col>
        </el-row>
        <el-row :gutter="3" style="height: 50%;">
          <el-col :span="24">
            <div class="grid-content bg-purple-light">
              <el-progress
                  :percentage="progress.submit"
                  stroke-linecap="butt"
                  type="line"
                  :stroke-width="7"
                  color="#e0e0e0"
                  :show-text="false"
              ></el-progress>
              <prompt-edit v-for="i in numCards" :key="i" :prompt="prompts[i-1]" :index="i-1" :ref="`promptEdit${i-1}`" @imageGenerated="handleImageGenerated" @taskStart="startTask" @taskComplete="completeTask" :selectedModel="selectedModel"/>
            </div>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span="17" class="overall">
        <el-row :gutter="3" class="outer" style="height: 20%;">
          <top-bar style="height: 100%; width:100%" :progress="progress"></top-bar>
        </el-row>
        <el-row :gutter="3" style="height: 80%;">
            <pic-view :count="count" :imageUrls="imageUrls"></pic-view>
        </el-row>
      </el-col>
    </el-row>
  </main>
</template>



<script>
import TopBar from '../components/TopBar.vue'
import InputView from '../components/InputView.vue'
import PicView from '../components/PicView.vue'
import PromptEdit from '../components/PromptEdit.vue'

export default {
  data() {
    return {
      selectedModel: 'deliberate_v2.safetensors', // 默认值
      progress: {
        style: 0,
        submit: 0,
        image: 100
      },
      count: 6,
      numCards: 0,
      prompts: [],
      imageUrls: []  // 给 imageUrls 一个初始值
    }
  },

  created() {
    this.handleChange(this.count);
  },
  methods: {
    updateSelectedOption(value) {
      this.selectedModel = value;
    },
    handleSubmit(prompts) {
      console.log(prompts);
      this.prompts = prompts;
    },
    handleChange(value) {
      this.count = value;
      this.numCards = value;
      for (let i = 0; i < 6; i++) {
        if (i < value) {
          this.prompts[i] = `prompt ${i + 1}`;
          this.imageUrls[i] = '';  // 或者你可以设置为默认的图片URL
        } else {
          this.prompts[i] = null;
          this.imageUrls[i] = null;  // 或者你可以设置为默认的图片URL
        }
      }
    },
    async handleAllGenerate() {
      for(let i = 0; i < this.prompts.length; i++) {
        await this.$refs[`promptEdit${i}`][0].generateImage();
      }
    },

    handleImageGenerated(index, imageUrl) {
      this.$set(this.imageUrls, index, imageUrl);
      console.log(this.imageUrls);
    },

    startTask(taskName) {
      let interval;
      let duration;
      this.progress[taskName] = 0;
      switch (taskName) {
        case 'style':
          duration = 25000; // 15s
          break;
        case 'submit':
          duration = 60000; // 50s
          break;
        case 'image':
          duration = 10000; // 6s
          break;

      }

      interval = setInterval(() => {
        if (this.progress[taskName] < 100) {
          this.progress[taskName] += 1;
        } else {
          clearInterval(interval);
        }
      }, duration / 100);
    },
    completeTask(taskName) {
      this.progress[taskName] = 100;
    }
  },
  components: {
    'top-bar': TopBar,
    'input-view': InputView,
    'pic-view': PicView,
    'prompt-edit': PromptEdit,

  },

  watch: {}

}
</script>

<style>
body, html {
  height: 100vh;
  padding: 0px;
  margin: 0px;
  background-color: #e5e9f2;
  overflow: auto;
}

main {
  height: 100vh;
}

.overall {
  height: 100%;
}

.detail {
  height: 100%;
  overflow: auto;
  -ms-overflow-style: none;
  overflow: -moz-scrollbars-none;
}

.detail::-webkit-scrollbar {
  width: 0 !important
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #ffffff;
}

.grid-content {
  height: 100%;
  width: 100%;
}

.newgrid-content {
  height: 100%;
  width: 100%;
}

.row-bg {
  padding: 5px 0;
  background-color: #f9fafc;
}

</style>