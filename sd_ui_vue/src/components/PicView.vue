<template>
  <div class="grid-container">
    <div v-for="(imageUrl, i) in imageUrls" :key="i" class="card">
      <div class="image-wrapper">
        <el-image :src="imageUrl" class="center-image"></el-image>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    imageUrls: Array
  },
}
</script>

<style scoped>
.grid-container {
  display: grid;
  justify-items: center;
  align-items: center;
  height: 100%;
  width: 60%;
  padding: 1% 20%;
}

.card {
  width: 100%;
  height: 100%;
  min-width: 60px;
  min-height: 60px;
}

.image-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.center-image {
  max-width: 100%;
  max-height: 100%;
  display: block;
  margin: 0 auto;
}
</style>
