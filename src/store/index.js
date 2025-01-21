import { createStore } from 'vuex'
import axios from "axios"
import router from '@/router';


export default createStore({
  state: {
    
    url:"http://127.0.0.1:8000/",
    user_error:"",
    category: [],
    quest: [],
    searchQuery: '',
    like:"",
    user:null,
    isLoggedIn: false,

  },

  getters: {
    filteredQuestionsByName: state => {
      if (!state.searchQuery) {
        return state.quest; 
      }
      return state.quest.filter(question =>
        question.question.toLowerCase().includes(state.searchQuery)
      );
    }
  },
  mutations: {
    // ADD_ANSWER(state, { questionId, answer }) {
    //   const question = state.quest.find(q => q.id === questionId);
    //   if (question) {
    //     const newCommentId = question.comments.length + 1;
    //     question.comments.push({ id: newCommentId, ...answer });
    //   }
    // },
    // LIKE_ANSWER(state, obj) {
    //   console.log(obj);
    //   const question = state.quest.find(q => q.id === obj.quest_id);
    //   if (question) {
    //     const comment = question.comments.find(c => c.id === obj.answer_id);
    //     if (comment.good) {
    //       comment.like--;
    //     }else{
    //       comment.like++;
    //     }
    //     comment.good = !comment.good
    //   }
    // },
    // LIKE_QUESTION(state, questionId) {
    //   const question = state.quest.find(q => q.id === questionId);
    //   if (question.good) {
    //     question.likes--;
    //   }else{
    //     question.likes++
    //   }
    //   question.good = !question.good
    // },
    TOGGLE_HEART_COLOR(state, { questionId, commentId }) {
      const question = state.quest.find(q => q.id === questionId);
      if (question) {
        const comment = question.comments.find(c => c.id === commentId);

        comment.good = !comment.good;
        comment.good ? comment.like++ : comment.like--;


      }
    },
    TOGGLE_QUESTION_HEART(state, questionId) {
      const question = state.quest.find(q => q.id === questionId);
      question.good = !question.good;
      question.good ? question.likes++ : question.likes--;
    },


    // ADD_COMMENT(state, obj) {
    //   const question = state.quest.find(q => q.id === obj.quest_id);
    //   if (question) {
    //     question.comments.push({ id: Math.floor(Math.random() * 1000), ...obj.comment, good: false, like: 0 });
    //   }
    // },
    SET_SEARCH_QUERY(state, query) {
      state.searchQuery = query;
    },


    change_user_error(state, obj) {
      state.user_error = obj;

    },
    setCategories(state, categories) {
      state.category = categories;
    },
    addquest(state, obj) {
      state.quest.push(obj);
    },

    getallquest(state, obj) {
      state.quest = obj;

    },

    add_Answer(state, obj) {
      state;
      console.log("obj", obj);
      const question = state.quest.find(q => q.id === obj.question_id);
      console.log(question);
      question.comments.push(obj);


    },

    like_quest(state, obj) {
      const a = state.quest.find(elm => elm.id === obj.id);
      a.likes = obj.likes;
      a.good = obj.good



    },
  

    likeAnswer(state, data) {
      state;
      console.log(data);
      let x = state.quest.find(elm => elm.id == data.question_id);
      let y = x.comments.find(elm => elm.id == data.id);
      y.good = data.good
      y.likes =data.likes
    },

    change_user(state, obj) {
      state.user = obj;
    },
    SET_LOGOUT(state) {
      state.isLoggedIn = false;
      state.user = null;
    }
  },


 


  actions: {
    async sign_up({state,commit},obj){
      try{
        let data = await axios.post(state.url+"sign_up/", obj)
        console.log(data);
        router.push({name:"sign_in"})
      }
      catch(err){
        console.log(err.response.data.errors);
        commit("change_user_error", err.response.data.errors)
      }
    },

    async sign_in({state, commit},obj){
      try{
        let {data} = await axios.post(state.url+"sign_in/", obj)
        console.log(data);
        localStorage.token=data.token
        router.push({name: "home"})
      }
      catch(err){
      console.log(err.response.data.message);
      commit("change_user_error", err.response.data)
      }
    },

    async add_question({ state ,commit}, obj) {
      console.log("obj", obj);
      try {
        let config = {
          headers: { 
            
            'Authorization': `Token ${localStorage.token}` },
        };

        console.log(config);
        let {data} = await axios.post(state.url + "add_question/", obj, config);
        console.log(data);
        commit("addquest",data)
      } catch (err) {
        console.log(err);
      }
    },

    async get_all_category({state,commit}){
      let config = {
        headers: { 
          'Authorization': `Token ${localStorage.token}` },
      };
      let {data} = await axios.get(state.url + "all_category/", config);
        console.log(data);
        commit("setCategories",data)

    },

    async get_all_quest({state,commit}){
      let config = {
        headers: { 
          'Authorization': `Token ${localStorage.token}` },
      };
      let {data} = await axios.get(state.url + "get_all_questions/", config);
      console.log(data);
      commit("getallquest",data)


    },
    async addAnswer({ state,commit }, obj) {
        let config = {
          headers: { 
            'Authorization': `Token ${localStorage.token}` },
        };

        const{data} = await axios.post(`${state.url}add_answer/`, obj, config);
        console.log(data);
        commit('add_Answer', data);

      } ,
    



    async like_question({ state, commit }, obj) {
      try {
        let config = {
          headers: {
            'Authorization': `Token ${localStorage.token}`
          }
        };
        let { data } = await axios.post(`${state.url}like_question/`, {id : obj}, config);
        console.log(data);
        commit("like_quest", data);
      } 
      catch (error) {
        console.error('Error in like_question action:', error);
        throw error; 
      }
    },

    async like_answer({state,commit}, obj){
      try{
        let config = {
          headers: {
            'Authorization': `Token ${localStorage.token}`
          }
        };
        let {data} = await axios.post(`${state.url}like_answer/`,{id:obj}, config);
        console.log(data);
        commit("likeAnswer",data);
      }
      catch(error){
        console.error('Error in like_answer action:', error)
        throw error;
      }
    },
    async get_user({ state, commit }) {
      try {
        let config = {
          headers: {
            'Authorization': `Token ${localStorage.token}`
          }
        };
        let { data } = await axios.get(state.url + "user/", config);
        console.log("data: user", data.user);
        commit("change_user", data.user);
        return data.user;
    
      } catch (error) {
        console.error("Error fetching user:", error);
      }
    }
,    

    logout({state, commit }) {
      return new Promise((resolve, reject) => {
        axios.post(`${state.url}log_out/`)
          .then(response => {
            commit('SET_LOGOUT');
            localStorage.removeItem('token');
            router.push('/sign_in');
            resolve(response.data.message); 
          })
          .catch(error => {
            reject(error); 
          });
      });
    }






  },
  modules: {},
});


