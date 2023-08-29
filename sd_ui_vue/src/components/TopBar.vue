<template>
  <el-row :gutter=0 style="width: 100%; display: flex; align-items: center;">

    <el-col :span=24 style="display: flex; align-items: center; justify-content: center; height: 100%;">
      <div class="grid-content bg-purple" style="padding: 0; margin: 0; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 40px;">STORY</span>
        <!--<el-progress :percentage="progress.style" stroke-linecap="butt" type="circle" :width="40" :stroke-width="20" color="#d7191c" :text-inside="true" :format="percentage => 'style'"></el-progress>
        <el-progress :percentage="progress.submit" stroke-linecap="butt" type="circle" :width="40" :stroke-width="20" color="#abdda4" :text-inside="true" :format="percentage => 'prompt'"></el-progress>-->
        <span style="font-size: 40px; margin-left: 10px; color: #fdae61;">DIFFUSI</span>
        <el-progress
            :percentage="progress.image"
            stroke-linecap="butt"
            type="circle"
            :width="32"
            :stroke-width="16"
            color="#fdae61"
            :text-inside="true"
            :format="percentage => 'image'"
        ></el-progress>
        <span style="font-size: 40px; color: #fdae61;">N</span>
      </div>
    </el-col>
  </el-row>
</template>



<script>
export default {
  props: ['progress'],

}

</script>

<style scoped>

.el-row {
  margin-bottom: 2px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 0px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #484848;
}
.bg-purple-light {
  background: #ffffff;
}
.grid-content {
  border-radius: 1px;
  min-height: 76px;
}
.row-bg {
  padding: 2px 0;
  background-color: #f9fafc;
}
</style>
