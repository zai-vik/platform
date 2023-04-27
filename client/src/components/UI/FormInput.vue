<template>
    <div
        :class="{ '--error' : error }"
    >
        <p>
            <slot></slot>
        </p>
        <input 
            type="text"
            @input="validate()"
            v-model.trim="input_value"
        >
        <p v-if="error" class="error-message">
            {{ error_message }}
        </p>
    </div>
</template>

<script>
export default {
    name: 'form-input',
    props: [
        'input_type',
        'input_auth'
    ],
    data() {
        return {
            input_value: '',
            error: false,
            error_message: '',

            // опции для логина
            login_error_symbols: '-@$&!=+,./|#%^*()\\{}[]\'";:<>?',
            min_login_length: 6,
            max_login_length: 20,
            rus_alphabet: 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя',

            // опции для email
            email_regexp: /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/iu
        }
    },  
    methods: {
        // Валидация
        validate() {
            if (this.input_auth === 'reg') {
                // Если поле логин
                if (this.input_type === 'login') {
                    // По длине логина
                    if (this.input_value.length < this.min_login_length) { // мин длина
                        this.error = true;
                        this.error_message = `Никнейм должен быть не меньше ${this.min_login_length} символов`;
                        return false;
                    } else if (this.input_value.length > this.max_login_length) { // макс длина
                        this.error = true;
                        this.error_message = `Никнейм должен быть не больше ${this.max_login_length} символов`;
                        return false;

                    } else if (this.loginErrorSymbols()) { // По содержанию запрещённых символов
                        this.error = true;
                        this.error_message = `Никнейм содержит недопустимые символы`;
                        return false;

                    } else if (this.errorRusAlphabet()) { // По содержанию кириллицы
                        this.error = true;
                        this.error_message = 'Никнейм не может содержать кириллицу';
                        return false;

                    } else {
                        this.error = false;
                    }

                } else if (this.input_type === 'email') { // Если поле email
                    const emailValid = () => {
                        return this.email_regexp.test(this.input_value);
                    }
                    if (!emailValid()) {
                        this.error = true;
                        this.error_message = 'Вы ввели некорректный email';
                    } else {
                        this.error = false;
                    }
                }
            }
        },
        loginErrorSymbols() {
            let include;
            let symbols = this.login_error_symbols.split('');
            symbols.forEach(symbol => {
                if (this.input_value.includes(symbol)) {
                    include = true;
                }
            })
            return include;
        },
        errorRusAlphabet() {
            let include;
            let alphabet = this.rus_alphabet.split('');
            alphabet.forEach(letter => {
                if (this.input_value.includes(letter)) {
                    include = true;
                }
            })
            return include;
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

    input {
        width: 400px;
        font-size: 16px;
        padding: 10px 15px;
        border-radius: 5px;
        border: 1px solid rgb(2, 2, 2);
        outline: none;
        transition: all .3s;
    }
    input:focus {
        transform: scale(1.05);
        box-shadow: 0 0 10px #b188f3af;
        margin-top: 5px;
    }

    .error-message {
        margin-bottom: 3px;
        max-width: 400px;
        font-size: 14px;
    }
</style>