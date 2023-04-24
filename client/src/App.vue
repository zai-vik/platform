<template>
  <div class="app">
    <router-view></router-view>
  </div>
</template>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Montserrat";
  font-weight: 700;
}

#app {
  background: rgb(189, 182, 230);
  background: linear-gradient(153deg, rgba(205, 200, 237, 0.811) 0%, rgba(229, 216, 255, 0.82) 31%, rgba(218, 213, 240, 0.825) 78%);
  width: 100vw;
  min-height: 100vh;
  font-family: "Montserrat";
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}
</style>
