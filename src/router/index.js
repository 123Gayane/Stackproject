import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "../views/HomePage.vue"
import AddQuestion from "../views/AddQuestion.vue"
import QuestionDetail from "../views/QuestionDetail.vue"
import SignIn from '@/views/SignIn.vue'
import SignUp from "../views/SignUp.vue"
import store from '@/store'


const metadata =  store
console.log(metadata);

const routes = [
  {
    path: "/home",
    component: HomePage,
    name: "home",
    meta: { requiresAuth: true } 
  },
  {
    path: "/add",
    component: AddQuestion,
    name: "add",
    meta: { requiresAuth: true } 
  },
  {
    path: '/question/:id',
    name: 'QuestionDetail',
    component: QuestionDetail,

  },
  {
    path: '/sign_in',
    name: 'sign_in',
    component: SignIn,
    meta: {check: true}

  },
  {
    path: '/',
    name: 'sign_up',
    component: SignUp,
    meta: {check: true}
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {

  if(to.meta.check){
    if(localStorage.token){
      try{
        await metadata.dispatch("get_user").then(r=>{
          if(r){
            next("/home")
          }
        })
        
      }catch(err){
        next("/sign_in")
      }
  }
}

  if (to.meta.requiresAuth){
    if(localStorage.token){
      try{
        await metadata.dispatch("get_user").then(r=>{
          if(r){
            next()
          }
        })
        
      }catch(err){
        next("/sign_in")
      }
    }else{
      next("/sign_in")
    }

  }else{
    next()
  }


  if (to.meta.requiresAuth && !store.state.isLoggedIn) {
    next('/sign_in'); 
  } else {
    next();
  }
})






export default router


