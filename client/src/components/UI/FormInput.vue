<template>
    <div>
        <p>
            <slot></slot>
        </p>
        <input type="text">
    </div>
</template>

<script>
export default {
    name: 'form-input'
}
</script>

<style scoped lang="scss">
    div {
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 5px;
        .--error {
            input {
                box-shadow: 0 0 10px #eb211693;
            }
        }
    }

    p {
        font-size: 18px;
    }

    input {
        width: 400px;
        font-size: 16px;
        padding: 10px 15px;
        border-radius: 5px;
        border: 1px solid rgb(2, 2, 2);
        outline: none;
        transition: .3s;
    }
    input:focus {
        transform: scale(1.05);
        box-shadow: 0 0 10px #b188f3af;
        margin-top: 5px;
    }
</style>