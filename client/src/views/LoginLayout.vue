<template>
    <div class="layout">
        <div class="main-container">
            <div class="container">
                <div class="left">
                    <img src="../img/LoginLayout/login_image_bg.png" alt="phone on hand">
                </div>
                <div class="right">
                    <form-login></form-login>
                </div>
            </div>
        </div>
        <div class="decoration">
            <img src="../img/krug_decoration.png" alt="">
            <img src="../img/krug_decoration.png" alt="">
            <img src="../img/krug_decoration.png" alt="">
            <img src="../img/krug_decoration.png" alt="">
            <img src="../img/krug_decoration.png" alt="">
        </div>
    </div>
</template>

<script>
import FormLogin from '@/components/FormLogin.vue'
export default {
  components: { FormLogin },

}
</script>

<style lang="scss" scoped>
.layout {
  width: 90vw;
  max-width: 1200px;
  height: 90vh;
  max-height: 800px;
  position: relative;
}

.main-container {
  width: 100%;
  height: 100%;
  background-color: #fff;
  border-radius: 30px;
  overflow: hidden;
  z-index: 1;
  position: relative;
  ::after {
    content: '';
    width: 100%;
    height: 100%;
    background-image: url(../img/abstract-white-background-with-dynamic-wavy-lines_23-2149116412.avif);
    background-size: cover;
    opacity: .05;
    position: absolute;
    top: 0;
    left: 0;
    z-index: -1;
  }
}

.decoration {
  img {
    position: absolute;
  }
  img:nth-child(1) {
    top: -120px;
    left: -180px;
  }
  img:nth-child(2) {
    transform: scale(.5);
    bottom: -200px;
    right: -230px;
    opacity: .7;
  }
  img:nth-child(3) {
    transform: scale(.2);
    bottom: 304px;
    right: -310px;
    opacity: .5;
  }
  img:nth-child(4) {
    transform: scale(.15);
    bottom: 304px;
    right: -194px;
    opacity: .7;
  }
  img:nth-child(5) {
    transform: scale(.3);
    bottom: -80px;
    left: -354px;
    opacity: .7;
  }
}

.container {
    display: flex;
    position: relative;
    width: 100%;
    height: 100%;
}

.left {
    width: 700px;
    height: 100%;
    position: relative;
    img {
        width: inherit;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }
}
.right {
    height: 100%;
    display: flex;
    justify-content: center;
    padding-right: 100px;
}
</style>