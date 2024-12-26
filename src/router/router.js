import { createRouter, createWebHistory } from 'vue-router'
import Main from "@/pages/Main"
import About from "@/pages/About"
import Link from "@/pages/Link"
import ChooseContent from "@/pages/ChooseContent"
const routes = [
  {
    path: '/',
    component: Main
  },
  {
    path: '/link',
    component: Link
},
{
    path: '/about',
    component: About
},

{
    path: '/choosecontent',
    component: ChooseContent
},

  
]

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL)
})

export default router;
