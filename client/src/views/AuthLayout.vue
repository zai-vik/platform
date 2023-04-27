<template>
    <div class="layout">
        <div class="main-container">
            <div class="container">
                <div class="left">
                    <img src="../img/LoginLayout/login_image_bg.png" alt="phone on hand">
                </div>
                <div class="right">
                    <router-view></router-view>
                </div>
            </div>
        </div>
        <div class="decoration">
            <img class="decor__img" src="../img/krug_decoration.png" alt="">
            <img class="decor__img" src="../img/krug_decoration.png" alt="">
            <img class="decor__img" src="../img/krug_decoration.png" alt="">
            <img class="decor__img" src="../img/krug_decoration.png" alt="">
        </div>
    </div>
</template>

<script>
import FormLogin from '@/components/FormLogin.vue'
export default {
  components: { FormLogin },
  mounted() {
    window.addEventListener('load', () => {
        const parallax = document.querySelector('.layout');
        if (parallax) {
            const images = document.querySelectorAll('.decor__img');

            const coeff_1 = 8,
            coeff_2 = 5,
            coeff_3 = 15,
            coeff_4 = 20;

            const speed = 0.05;

            let positionX = 0, positionY = 0;
            let coordXprocent = 0, coordYprocent = 0;

            function setMouseParallaxStyle() {
                const distX = coordXprocent - positionX;
                const distY = coordYprocent - positionY;

                positionX = positionX + (distX * speed);
                positionY = positionY + (distY * speed);

                images[0].style.cssText = `transform: translate(${positionX / coeff_1}%, ${positionY / coeff_1}%)`;
                images[1].style.cssText = `transform: translate(${positionX / coeff_2}%, ${positionY / coeff_2}%) scale(.5)`;
                images[2].style.cssText = `transform: translate(${positionX / coeff_3}%, ${positionY / coeff_3}%) scale(.2)`;
                images[3].style.cssText = `transform: translate(${positionX / coeff_4}%, ${positionY / coeff_4}%) scale(.3)`;

                requestAnimationFrame(setMouseParallaxStyle);
            }
            setMouseParallaxStyle();

            parallax.addEventListener('mousemove', (e) => {
                const parallaxWidth = parallax.offsetWidth;
                const parallaxHeight = parallax.offsetHeight;

                const coordX = e.pageX - parallaxWidth / 2;
                const coordY = e.pageY - parallaxHeight / 2;

                coordXprocent = coordX / parallaxWidth * 100;
                coordYprocent = coordY / parallaxHeight * 100;
            })
        }
    })
  }
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
    opacity: .03;
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
        pointer-events: none;
    }
}
.right {
    height: 100%;
    display: flex;
    justify-content: center;
    padding-right: 100px;
}
</style>