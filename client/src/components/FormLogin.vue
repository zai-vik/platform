<template>
    <div class="container-form">
        <h1>Авторизация</h1>
        <form>
            <form-input data-name="login" class="input">Логин</form-input>
            <form-input-pass data-name="password" class="input">Пароль</form-input-pass>
            <main-btn type="button" @click="Login()" class="btn">Войти</main-btn>
        </form>
        <div class="block">
            {{ get }}
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            path: '@/api/login/login.php',
            get: null
        }
    },
    methods: {
        Login() {
            let login = document.querySelector('[data-name="login"] input').value;
            console.log(login)
            let password = document.querySelector('[data-name="password"] input').value;
            console.log(password)
            const axios = require('axios');
            axios.post('http://localhost:8081/api/login', {'login': login, 'password': password}).then(response => {
                    this.get = response.data;
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
    }

    form {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .input {
        margin-top: 20px;
    }

    .btn {
        width: 200px;
        margin-top: 30px;
    }
</style>