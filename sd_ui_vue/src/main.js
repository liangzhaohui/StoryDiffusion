import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import i18n from './i18n';
import axios from 'axios';

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

Vue.config.productionTip = false

// 定义全局的HTTP链接
const apiUrl = 'http://127.0.0.1';
Vue.prototype.$apiUrl = 'http://127.0.0.1';
Vue.prototype.$saveLogToServer = function(logMessage) {
  axios.post(`${apiUrl}:5010/api/save-log`, {
    log: logMessage
  }).then(response => {
    // Log saved in server
  }).catch(error => {
    // Handle error
  });
};

new Vue({
  router,
  store,
  i18n,
  render: h => h(App)
}).$mount('#app')

