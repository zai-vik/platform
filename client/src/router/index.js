import { createRouter, createWebHistory } from 'vue-router'

import MainPage from '@/views/MainPage';
import AuthLayout from '@/views/AuthLayout';

import FormLogin from '@/components/FormLogin';
import FormReg from '@/components/FormReg';


const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPage
  },
  {
    path: '/login',
    name: 'loginLayout',
    component: AuthLayout,
    children: [
      {
        path: '',
        name: 'login',
        component: FormLogin
      }
    ]
  },
  {
    path: '/reg',
    name: 'regLayout',
    component: AuthLayout,
    children: [
      {
        path: '',
        name: 'reg',
        component: FormReg
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
