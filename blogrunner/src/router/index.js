import Vue from 'vue'
import Router from 'vue-router'
import spider from '@/components/spider'
import result from '@/components/result'
import check from '@/components/check'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/spider',
      name: 'spider',
      component: spider
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
