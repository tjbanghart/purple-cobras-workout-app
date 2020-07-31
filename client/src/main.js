/*!

=========================================================
* Vue Argon Design System - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-design-system
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-design-system/blob/master/LICENSE.md)

* Coded by www.creative-tim.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Argon from "./plugins/argon-kit";
import BootstrapVue from 'bootstrap-vue'
import './registerServiceWorker'
import axios from 'axios'
import moment from 'moment'

Vue.config.productionTip = false;
Vue.use(Argon);
Vue.use(BootstrapVue);

Vue.prototype.$http = axios;
Vue.prototype.$moment = moment;

Vue.prototype.$localStorage = new Vue({
  data: { 
     authToken: window.localStorage.getItem('authToken') 
  },
  watch:{ 
     authToken(value){ window.localStorage.setItem('authToken', value) } 
  }
})


new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
