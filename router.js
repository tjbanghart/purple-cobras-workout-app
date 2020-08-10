import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Category from './views/Category.vue'
import Topic from './views/Topic.vue'
import CreateTopic from './views/CreateTopic.vue'
import NotFound from './views/NotFound.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/c/:categorySlug',
      name: 'Category',
      component: Category
    },
    {
      path: '/t/:topicId',
      name: 'Topic',
      component: Topic
    },
    {
      path: '/c/:categorySlug/new-topic',
      name: 'CreateTopic',
      component: CreateTopic,
      meta: { auth: true }
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
