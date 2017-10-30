import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import result from '@/components/result'
import check from '@/components/check'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: HelloWorld
    }, {
      path: '/result',
      name: 'result',
      component: result
    }, {
      path: '/check',
      name: 'check',
      component: check
    }
  ]
})
