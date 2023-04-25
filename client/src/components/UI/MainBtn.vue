<template>
  <button>
    <slot></slot>
  </button>
</template>

<script>
export default {
    name: 'main-btn'
}
</script>

<style scoped lang="scss">
    button {
        border: 1px solid rgba(2, 2, 2);
        color: rgba(2, 2, 2);
        background: none;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: .3s;
    }
    button:hover {
        border-color: #b188f3;
        background-color:  #b188f3;
        color: #fff;
    }
</style>