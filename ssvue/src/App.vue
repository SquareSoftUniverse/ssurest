<template>
  <div id="nav">
    <router-link to="/">Home</router-link>
    <!-- <router-link to="/about">About</router-link> -->
  </div>
  <router-view />
</template>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

body {
  background-image: url("./assets/stars.jpg");
}

#nav {
  padding: 30px;
  align-content: center;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
