<template>
  <div class="home">
    <h2>欢迎来到 Mixcraft</h2>
    <p>智能歌单构建、作品展示、个人主页</p>
    <div class="features">
      <div class="feature-card">
        <h3>🎵 智能歌单</h3>
        <p>AI辅助创建完美的DJ歌单</p>
      </div>
      <div class="feature-card">
        <h3>🎧 作品展示</h3>
        <p>分享你的混音作品</p>
      </div>
      <div class="feature-card">
        <h3>👤 个人主页</h3>
        <p>打造专属DJ形象</p>
      </div>
    </div>
  </div>
</template>

<script setup>
// Home component
</script>

<style scoped>
.home {
  max-width: 800px;
  margin: 0 auto;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.feature-card {
  padding: 20px;
  background: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.feature-card h3 {
  margin-top: 0;
  color: #667eea;
}
</style>
