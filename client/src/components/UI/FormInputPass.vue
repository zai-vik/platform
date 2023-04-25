<template>
    <div
        :class="{ '--error' : error }"
    >
        <p>
            <slot></slot>
        </p>
        <span>
            <input 
                ref="input" 
                :type="type"
                @input="validate()"
                v-model.trim="input_value"
            >
            <div class="eye">
                <img @click="ShowPass()" :src="path" alt="eye">
            </div>
        </span>
        <p v-if="error" class="error-message">
            {{ error_message }}
        </p>
    </div>
</template>

<script>
export default {
    name: 'form-input-pass',
    data() {
        return {
            path: require("@/img/InputPass/eye_locked.png"),
            type: "password",
            input_value: '',
            error: false,
            error_message: '',
            min_pass_length: 6,
            pass_regexp: /([a-z]+[A-Z]+[0-9]+|[a-z]+[0-9]+[A-Z]+|[A-Z]+[a-z]+[0-9]+|[A-Z]+[0-9]+[a-z]+|[0-9]+[a-z]+[A-Z]+|[0-9]+[A-Z]+[a-z]+)/
        }
    },
    props: [
        'input_type',
        'input_auth'
    ],
    methods: {
        ShowPass() {
            this.$refs.input.focus();
            if (this.path === require("@/img/InputPass/eye_locked.png")) {
                this.path = require("@/img/InputPass/eye.png");
                this.type = "text";
            } else {
                this.path = require("@/img/InputPass/eye_locked.png");
                this.type = "password";
            }
        },
        validate() {
            if (this.input_auth === 'reg') {
                if (this.input_type === 'password') {
                    const passValid = () => {
                        return this.pass_regexp.test(this.input_value);
                    }
                    if (this.input_value.length < this.min_pass_length) {
                        this.error = true;
                        this.error_message = `Пароль должен быть не менее ${this.min_pass_length} символов`;
                        return false;
                    } else if (!passValid()) {
                        this.error = true;
                        this.error_message = 'Пароль должен содержать цифры и буквы(заглавные и строчные)';
                        return false;
                    } else {
                        this.error = false;
                    }
                } else if (this.input_type === 'password-double') {
                    const password_input = document.querySelector('[data-name="password"] input');
                    if (this.input_value !== password_input.value) {
                        this.error = true;
                        this.error_message = 'Пароли не совпадают';
                        return false;
                    } else {
                        this.error = false;
                    }
                }
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
            p {
                color: #eb2116d6;
            }
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

    .error-message {
        margin-bottom: 3px;
        max-width: 400px;
        font-size: 14px;
    }
</style>