import Vue from 'vue'
import Router from 'vue-router'
import aboutus from '@/components/aboutus'
// import spider from '@/components/spider'
import result from '@/components/result'
import urlupload from '@/components/urlupload'
import htmlupload from '@/components/htmlupload'
import check from '@/components/check'
import website from '@/components/website'
import keyword from '@/components/keyword'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'root',
      component: keyword
    }, {
      path: '/keyword',
      name: 'keyword',
      component: keyword
    }, {
      path: '/urlupload',
      name: 'urlupload',
      component: urlupload
    }, {
      path: '/htmlupload',
      name: 'htmlupload',
      component: htmlupload
    }, {
      path: '/check',
      name: 'check',
      component: check
    }, {
      path: '/website',
      name: 'website',
      component: website
    }, {
      path: '/result',
      name: 'result',
      component: result
    }, {
      path: '/aboutus',
      name: 'aboutus',
      component: aboutus
    }
  ]
})
