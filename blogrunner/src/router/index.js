import Vue from 'vue'
import Router from 'vue-router'
// import spider from '@/components/spider'
import result from '@/components/result'
import check from '@/components/check'
import website from '@/components/website'
import keyword from '@/components/keyword'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/keyword',
      name: 'keyword',
      component: keyword
    }, {
      path: '/result',
      name: 'result',
      component: result
    }, {
      path: '/check',
      name: 'check',
      component: check
    }, {
      path: '/website',
      name: 'website',
      component: website
    }
  ]
})
