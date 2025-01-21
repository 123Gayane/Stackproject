// import { createApp } from 'vue'
// import App from './App.vue'
// import router from './router'
// import store from './store'
import './index.css'


// createApp(App).use(store).use(router).mount('#app')
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import { configure } from 'vee-validate';

const app = createApp(App);

configure({
  generateMessage: (ctx) => {
    return `${ctx.field} is required.`;
  },
});

app.use(store).use(router).mount('#app');
