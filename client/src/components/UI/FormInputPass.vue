<template>
    <div>
        <p>
            <slot></slot>
        </p>
        <span>
            <input id="password_input" :type="type">
            <label for="password_input">
                <div class="eye">
                    <img @click="ShowPass()" :src="path" alt="eye">
                </div>
            </label>
        </span>
    </div>
</template>

<script>
export default {
    name: 'form-input-pass',
    data() {
        return {
            path: require("@/img/InputPass/eye_locked.png"),
            type: "password"
        }
    },
    methods: {
        ShowPass() {
            if (this.path === require("@/img/InputPass/eye_locked.png")) {
                this.path = require("@/img/InputPass/eye.png");
                this.type = "text";
            } else {
                this.path = require("@/img/InputPass/eye_locked.png");
                this.type = "password";
            }
        }
    }
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

    span {
        position: relative;
        width: 400px;
    }

    input {
        width: 100%;
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

    .eye {
        img {
            width: 25px;
            position: absolute;
            right: 10px;
            top: 5px;
            bottom: 0;
            margin: auto;
            cursor: pointer;
        }
    }
</style>