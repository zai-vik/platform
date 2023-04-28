<template>
    <div class="container-form">
        <h1>Регистрация</h1>
        <form>
            <form-input 
                data-name="login"
                :input_type=" 'login' " 
                :input_auth=" 'reg' "
                class="input"
            >
                Никнейм
            </form-input>

            <form-input    
                data-name="email" 
                :input_type=" 'email' " 
                :input_auth=" 'reg' "
                class="input"
            >
                Email
            </form-input>

            <form-input-pass 
                data-name="password" 
                :input_type=" 'password' " 
                :input_auth=" 'reg' "
                class="input"
            >
                Пароль
            </form-input-pass>

            <form-input-pass 
                data-name="password-double" 
                :input_type=" 'password-double' " 
                :input_auth=" 'reg' " 
                class="input"
            >
                Повторите пароль
            </form-input-pass>

            <main-btn type="button" @click="Register()" class="btn">Зарегистрироваться</main-btn>
        </form>
        <div>{{ get }}</div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            path: 'http://127.0.0.1:8081/api/reg',
            login: '',
            email: '',
            password: '',
            password_double: '',
            get: null
        }
    },
    methods: {
        Register() {
            let login = document.querySelector('[data-name="login"] input').value;
            console.log(login)
            let password = document.querySelector('[data-name="password"] input').value;
            console.log(password)
            let email = document.querySelector('[data-name="email"] input').value;
            console.log(email)
            const axios = require('axios');
            axios.post(this.path, {'login' : login, 'email' : email, 'password' : password}).then(response => {
                this.get = response.data.message;
            })
            .catch(err => {
                this.get = err;
            })
        }
    }
}
</script>

<style scoped lang="scss">
    .container-form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    h1 {
        font-weight: 600;
        text-align: center;
        margin-bottom: 10px;
    }

    form {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .input {
        margin-top: 10px;
    }

    .btn {
        margin-top: 25px;
    }
</style>