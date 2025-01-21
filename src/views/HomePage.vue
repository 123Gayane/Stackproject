<template>
  <div class="w-full md:w-2/3 mx-auto p-5 bg-white rounded-lg shadow">
    <div class="flex items-center justify-between">
      <div class="w-full">
        <h2 class="section-heading text-bold">
          Questions and Answer
        </h2>
      </div>
    </div>

    <div class="mt-8 space-y-8">
      <div  v-for="question in filteredQuestionsByName" :key="question.id">
        <div>
          <div class="flex items-center mb-5">
              <div class="mr-2 w-6 h-6 overflow-hidden shadow rounded-full border-gray-500">
                <div class="w-full h-full bg-gray-200"></div>
              </div>
              <span class="text-sm text-gray-800">
                {{ question.user.name }}
                <span class="hidden md:inline-block">- 2 days ago</span>
              </span>
            </div>
          <div class="flex items-start">
            <div>
              <span class="inline-flex justify-center items-center w-6 h-6 rounded bg-green-500 text-white font-medium text-sm">
                Q
              </span>
            </div>
            <p class="ml-4 md:ml-6 text-bold">
              {{ question.isExpanded ? question.question : truncatedQuestion(question.question) }}
              <button v-if="question.question.length > 30" @click.stop="toggleQuestionExpansion(question.id)">
                {{ question.isExpanded ? 'See Less' : 'See More' }}
              </button>
            </p>
          </div>

          <div class="flex items-start mt-3 ml-10 gap-2" v-for="answer in question.comments" :key="answer.id">
            <div>
              <span class="inline-flex justify-center items-center w-6 h-6 rounded bg-gray-200 text-gray-800 font-medium text-sm"> A </span>
            </div>
            <p class="ml-4 md:ml-6 text-bold text-gray-800">{{ answer.comment }} </p>
            <div class="flex justify-center items-center gap-1">
              <span class="smiley" @click="like_Answer(answer.id)">
                <span v-if="answer.good">❤️</span>
                <span v-else>🤍</span>
              </span>
              <span>{{ answer.likes}}</span>

            </div>
          </div> 

     
          <div class="gap-4 flex justify-center mt-8 flex-col">
            <div class="flex md:items-center bg-gray-100 hover:bg-gray-200 rounded-lg px-3 py-2 cursor-pointer group">
              <span class="heart" @click="likeQuest(question.id)">
                <span v-if="question.good">❤️</span>
                <span v-else>🤍</span>
                  {{ question.likes }}
             </span>  
            </div>

    <Form @submit="(values, actions) =>add_answer(values, question.id, actions)" :validation-schema="schema">  
      <div class="w-72 flex">
      <div class="relative w-full min-w-[200px] h-10 flex justify-center items-center">
     <Field
      name="comment"
      class="peer w-full h-full bg-transparent text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
      placeholder=" " > </Field>
    <ErrorMessage name="comment"/>
     <label
      class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900">commment
    </label>


  </div>

      <button class="align-middle select-none font-sans font-bold text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 px-6 rounded-lg bg-gray-900 text-white shadow-md shadow-gray-900/10 hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none">
        Button
       </button> 

</div>  
</Form> 

          </div>
        </div>
      </div>
    </div>
  </div> 
</template> 

<script>
import { mapState, mapActions, mapMutations, mapGetters } from 'vuex';
import {Form, Field} from "vee-validate"
import * as yup from "yup"
export default {

  components:{
    Form, Field
  },
  data() {
    return {
      searchQuery: '',
      expandedQuestions: [],
      newReply: '',
    };
  },
  mounted(){
    this.get_all_quest()
    

  },


  computed: {
    ...mapState(['quest','comments']),
    ...mapGetters(["filteredQuestionsByName"]),

    schema(){
      return yup.object({
        comment: yup.string().required()
      })
    },


    filteredQuestions() {
      return this.quest
        .filter(question =>
          question.question.toLowerCase().includes(this.searchQuery.toLowerCase())
        )
        .map(question => ({
          ...question,
          isExpanded: this.expandedQuestions.includes(question.id)
        }));
    },
  },

  methods: {
    ...mapActions(['toggleQuestionHeart', 'toggleHeartColor', 'get_all_quest','like_question','addAnswer','like_answer']),
    ...mapMutations([ "LIKE_ANSWER","LIKE_QUESTION"]),

    truncatedQuestion(question) {
      return question.length > 30 ? question.substring(0, 30) + '...' : question;
    },


    toggleQuestionExpansion(id) {
      if (this.expandedQuestions.includes(id)) {
        this.expandedQuestions = this.expandedQuestions.filter(qid => qid !== id);
      } else {
        this.expandedQuestions.push(id);
      }
    },

  



      add_answer(comment, quest_id, {resetForm}) {
        comment.question_id = quest_id
        resetForm()
        console.log(comment);
        this.addAnswer(comment)
      },


      likeQuest(question_id){
        this.like_question(question_id)
      },

      like_Answer(answer_id){
        this.like_answer(answer_id)
      },


    toggleReplyForm(answerId) {
      const answer = this.findAnswerById(answerId);
      if (answer) {
        answer.showReplyForm = !answer.showReplyForm;
      }
    },


    submitReply(answerId) {
      const answer = this.findAnswerById(answerId);
      if (answer && this.newReply.trim()) {
        const newReply = {
          id: Date.now(),
          comment: this.newReply,
          like: 0,
          good: false,  
        };
        answer.replies = answer.replies || [];
        answer.replies.push(newReply);
        this.newReply = '';
      }
    },

  }

};
</script>














  
  


