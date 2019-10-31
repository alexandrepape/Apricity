import Vue from 'vue'
import Router from 'vue-router'
import ShowDemographic from '@/components/ShowDemographic'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/demo',
      name: 'demo',
      component: ShowDemographic
    }
  ]
})
