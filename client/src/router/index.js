import { createRouter, createWebHistory } from 'vue-router'

import MainPage from '@/views/MainPage';
import LoginLayout from '@/views/LoginLayout';


const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginLayout
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
