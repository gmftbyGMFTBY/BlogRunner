import Vue from 'vue'
import Router from 'vue-router'
import Result from '@/components/Result'
import Homepage from '@/components/Homepage'
import Aboutus from '@/components/Aboutus'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage
    },
    { path: '/Result',
      name: 'Result',
      component: Result
    },
    {
      path: '/About',
      name: 'About',
      component: Aboutus
    }
  ]
})
