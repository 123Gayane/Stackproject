<template>
  <nav  v-if="user" class="bg-white border-gray-200 dark:bg-gray-900">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <a href="#" class="flex items-center" >
        <img src="https://cdn.icon-icons.com/icons2/730/PNG/512/stackoverflow_icon-icons.com_62763.png" class="h-8 mr-3" alt="Flowbite Logo" />
        <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">StackOverflow</span>
      </a>
      <div class="relative md:block" >
        <input
      
          @input="search"
          v-model="check"

          type="text"
          class="mt-5 block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Search..."
        />
      </div>
      <div class="items-center justify-between w-full md:flex md:w-auto md:order-1" id="navbar-search">
        <div class="relative mt-3 md:hidden"></div>
        <ul class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
          <li>
            <router-link
      
              :to="{ name: 'home' }"
              class="block py-2 pl-3 pr-4 text-gray-900 rounded md:bg-transparent md:p-0 md:dark:text-white"
              active-class="text-blue-700 dark:text-blue-500"
              aria-current="page"
            >Home</router-link>
          </li>
          <li>
            <router-link
        
              :to="{ name: 'add' }"
              class="block py-2 pl-3 pr-4 text-gray-900 rounded md:bg-transparent md:p-0 md:dark:text-white"
              active-class="text-blue-700 dark:text-blue-500"
              aria-current="page"
            >Add Question</router-link>
          </li>
        </ul> <br>
        <button class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
            <span class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
           
                <button @click="logout">Logout</button>
           
             
                
            </span>
        </button>
      </div>
    </div>
  </nav>
  <router-view />
</template>

<script>
import { mapState,mapMutations,mapActions } from 'vuex';


export default {

  data(){
    return {
      check : ""
    }
  },
  
  computed: {
    ...mapState(['searchQuery','user','isLoggedIn']),
    
  },
  methods: {
    ...mapMutations(['SET_SEARCH_QUERY']),
    ...mapActions(['logout']),
    handleLogout() {
      this.logout().then(() => {
        this.$router.push('/sign_in'); 
        
      });
    },

    search(){
      this.SET_SEARCH_QUERY(this.check)

    }
  },
};
</script>




<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color:#333356;

}



nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

