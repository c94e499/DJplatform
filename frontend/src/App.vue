<template>
  <div id="app">
    <header class="app-header">
      <h1>Mixcraft DJ 创作平台</h1>
      <nav>
        <router-link to="/">首页</router-link>
        <router-link to="/about">关于</router-link>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script setup>
// Main App component
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.app-header {
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.app-header h1 {
  margin: 0 0 10px 0;
}

.app-header nav {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.app-header nav a {
  color: white;
  text-decoration: none;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background 0.3s;
}

.app-header nav a:hover {
  background: rgba(255, 255, 255, 0.2);
}

.app-header nav a.router-link-active {
  background: rgba(255, 255, 255, 0.3);
}

main {
  padding: 20px;
}
</style>
