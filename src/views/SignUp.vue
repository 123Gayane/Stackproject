<template>
    <section class="container">
      <div class="register-container">
        <div class="circle circle-one"></div>
        <div class="form-container">
          <img
            src="https://raw.githubusercontent.com/hicodersofficial/glassmorphism-login-form/master/assets/illustration.png"
            alt="illustration"
            class="illustration"
          />
          <h1 class="opacity">REGISTER</h1>
          <Form @submit="get_info" method="POST">
            <Field type="text" name="username" placeholder="USERNAME" />
            <Field type="email" name="email" placeholder="EMAIL" />
            <Field type="text" name="password1" placeholder="password1"/>
            <Field type="text" name="password2" placeholder="password2"/>
         
            <button class="opacity">SUBMIT</button>
          </Form>
          <div class="login opacity">
            <router-link to="/sign_in" class="nav-link">LOGIN</router-link>
          </div>
        </div>
        <div class="circle circle-two"></div>
      </div>
      <div class="theme-btn-container"></div>
    </section>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex';
  import { Field, Form } from 'vee-validate';
  
  export default {
    data() {
      return {
        themes: [
          {
            background: '#1A1A2E',
            color: '#FFFFFF',
            primaryColor: '#0F3460'
          },
          {
            background: '#461220',
            color: '#FFFFFF',
            primaryColor: '#E94560'
          },
          {
            background: '#192A51',
            color: '#FFFFFF',
            primaryColor: '#967AA1'
          },
          {
            background: '#F7B267',
            color: '#000000',
            primaryColor: '#F4845F'
          },
          {
            background: '#F25F5C',
            color: '#000000',
            primaryColor: '#642B36'
          },
          {
            background: '#231F20',
            color: '#FFF',
            primaryColor: '#BB4430'
          }
        ]
      };
    },
    mounted() {
      this.$nextTick(() => {
        this.displayThemeButtons();
      });
    },
    computed: {
      ...mapState(['user_error'])
    },
    components: {
      Form,
      Field
    },
    methods: {
      ...mapActions(['sign_up']),
      get_info(obj) {
        console.log(obj);
        this.sign_up(obj);
      },
      setTheme(theme) {
        const root = document.querySelector(':root');
        if (root) {
          root.style.setProperty('--background', theme.background);
          root.style.setProperty('--color', theme.color);
          root.style.setProperty('--primary-color', theme.primaryColor);
        }
      },
      displayThemeButtons() {
        const btnContainer = document.querySelector('.theme-btn-container');
        if (btnContainer) {
          this.themes.forEach((theme) => {
            const div = document.createElement('div');
            div.className = 'theme-btn';
            div.style.cssText = `background: ${theme.background}; width: 25px; height: 25px`;
            btnContainer.appendChild(div);
            div.addEventListener('click', () => this.setTheme(theme));
          });
        }
      }
    }
  };
  </script>
  


<style>
:root {
    --background: #333356;
    --color: #ffffff;
    --primary-color: #0f3460;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    box-sizing: border-box;
    font-family: "poppins";
    background: var(--background);
    color: var(--color);
    letter-spacing: 1px;
    transition: background 0.2s ease;
    -webkit-transition: background 0.2s ease;
    -moz-transition: background 0.2s ease;
    -ms-transition: background 0.2s ease;
    -o-transition: background 0.2s ease;
}

a {
    text-decoration: none;
    color: var(--color);
}

h1 {
    font-size: 2.5rem;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;  
    min-width: 200vh;   
}

.register-container {
    position: relative;
    width: 22.2rem;
}
.form-container {
    border: 1px solid hsla(0, 0%, 65%, 0.158);
    box-shadow: 0 0 36px 1px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    backdrop-filter: blur(20px);
    z-index: 99;
    padding: 2rem;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    -ms-border-radius: 10px;
    -o-border-radius: 10px;
}

.register-container form input {
    display: block;
    padding: 14.5px;
    width: 100%;
    margin: 2rem 0;
    color: var(--color);
    outline: none;
    background-color: #9191911f;
    border: none;
    border-radius: 5px;
    font-weight: 500;
    letter-spacing: 0.8px;
    font-size: 15px;
    backdrop-filter: blur(15px);
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
}

.register-container form input:focus {
    box-shadow: 0 0 16px 1px rgba(0, 0, 0, 0.2);
    animation: wobble 0.3s ease-in;
    -webkit-animation: wobble 0.3s ease-in;
}

.register-container form button {
    background-color: var(--primary-color);
    color: var(--color);
    display: block;
    padding: 13px;
    border-radius: 5px;
    outline: none;
    font-size: 18px;
    letter-spacing: 1.5px;
    font-weight: bold;
    width: 100%;
    cursor: pointer;
    margin-bottom: 2rem;
    transition: all 0.1s ease-in-out;
    border: none;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    -webkit-transition: all 0.1s ease-in-out;
    -moz-transition: all 0.1s ease-in-out;
    -ms-transition: all 0.1s ease-in-out;
    -o-transition: all 0.1s ease-in-out;
}

.register-container form button:hover {
    box-shadow: 0 0 10px 1px rgba(0, 0, 0, 0.15);
    transform: scale(1.02);
    -webkit-transform: scale(1.02);
    -moz-transform: scale(1.02);
    -ms-transform: scale(1.02);
    -o-transform: scale(1.02);
}

.circle {
    width: 8rem;
    height: 8rem;
    background: var(--primary-color);
    border-radius: 50%;
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    -ms-border-radius: 50%;
    -o-border-radius: 50%;
    position: absolute;
}

.illustration {
    position: absolute;
    top: -14%;
    right: -2px;
    width: 90%;
}

.circle-one {
    top: 0;
    left: 0;
    z-index: -1;
    transform: translate(-45%, -45%);
    -webkit-transform: translate(-45%, -45%);
    -moz-transform: translate(-45%, -45%);
    -ms-transform: translate(-45%, -45%);
    -o-transform: translate(-45%, -45%);
}

.circle-two {
    bottom: 0;
    right: 0;
    z-index: -1;
    transform: translate(45%, 45%);
    -webkit-transform: translate(45%, 45%);
    -moz-transform: translate(45%, 45%);
    -ms-transform: translate(45%, 45%);
    -o-transform: translate(45%, 45%);
}

.login {
    margin: 1rem 0;
    display: flex;
    justify-content: center;
}
.opacity {
    opacity: 0.6;
}

.theme-btn-container {
    position: absolute;
    left: 0;
    bottom: 2rem;
}

.theme-btn {
    cursor: pointer;
    transition: all 0.3s ease-in;
}

.theme-btn:hover {
    width: 40px !important;
}

@keyframes wobble {
    0% {
        transform: scale(1.025);
        -webkit-transform: scale(1.025);
        -moz-transform: scale(1.025);
        -ms-transform: scale(1.025);
        -o-transform: scale(1.025);
    }
    25% {
        transform: scale(1);
        -webkit-transform: scale(1);
        -moz-transform: scale(1);
        -ms-transform: scale(1);
        -o-transform: scale(1);
    }
    75% {
        transform: scale(1.025);
        -webkit-transform: scale(1.025);
        -moz-transform: scale(1.025);
        -ms-transform: scale(1.025);
        -o-transform: scale(1.025);
    }
    100% {
        transform: scale(1);
        -webkit-transform: scale(1);
        -moz-transform: scale(1);
        -ms-transform: scale(1);
        -o-transform: scale(1);
    }
}
</style>
    