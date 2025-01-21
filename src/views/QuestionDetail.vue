<template>
  <div class="container">
    <h1 class="title">{{ question.question }}</h1>
    <p class="category">Category: {{ question.category }}</p>
    <h3 class="answers-heading">Answers:</h3>
    <ul class="answers-list">
      <li v-for="comment in sortedComments" :key="comment.id" class="answer-item">
        <p>{{ comment.comment }}</p>
        <div class="answer-actions">
          <!-- <span class="like-count"> ❤️ : {{ comment.like }}</span> -->
          <span 
            class="smiley" 
            @click="toggleHeart(comment.id)"> 
            {{ comment.good ? '❤️' : '🤍' }} {{ comment.like }}
          </span>
        </div>
      </li>
    </ul>

    <div class="answer-form">
      <h3 class="add-answer-heading">Add a new answer</h3>
      <form @submit.prevent="submitAnswer" class="form">
        <div class="form-group">
          <label for="newAnswer" class="label">Your Answer:</label>
          <input
            type="text"
            v-model="newAnswer"
            id="newAnswer"
            class="input"
            placeholder="Enter your answer"
            required
          />
        </div>
        <button type="submit" class="submit-button">Submit</button>
      </form>
    </div>
    <div class="theme-btn-container"></div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  data() {
    return {
      newAnswer: '',
      themes: [
        {
          background: "#1A1A2E",
          color: "#FFFFFF",
          primaryColor: "#0F3460"
        },
        {
          background: "#461220",
          color: "#FFFFFF",
          primaryColor: "#E94560"
        },
        {
          background: "#192A51",
          color: "#FFFFFF",
          primaryColor: "#967AA1"
        },
        {
          background: "#F7B267",
          color: "#000000",
          primaryColor: "#F4845F"
        },
        {
          background: "#F25F5C",
          color: "#000000",
          primaryColor: "#642B36"
        },
        {
          background: "#231F20",
          color: "#FFF",
          primaryColor: "#BB4430"
        }
      ]
    };
  },
  computed: {
    ...mapState(['quest']),
    question() {
      return this.quest.find(question => question.id === parseInt(this.$route.params.id)) || {};
    },
    sortedComments() {
      return this.question.comments.slice().sort((a, b) => b.like - a.like);
    },
  },
  mounted() {
    this.displayButtons();
  },
  methods: {
    ...mapActions(['addAnswer', 'likeAnswer', 'toggleHeartColor']),
    submitAnswer() {
      const answer = {
        comment: this.newAnswer,
        like: 0,
        good: false
      };
      this.addAnswer({ questionId: this.question.id, answer });
      this.newAnswer = '';
    },
    toggleHeart(commentId) {
      this.toggleHeartColor({ questionId: this.question.id, commentId });
    },
    setTheme(theme) {
      const root = document.querySelector(":root");
      root.style.setProperty("--background", theme.background);
      root.style.setProperty("--color", theme.color);
      root.style.setProperty("--primary-color", theme.primaryColor);
    },
    displayButtons() {
      const btnContainer = document.querySelector(".theme-btn-container");
      this.themes.forEach((theme) => {
        const div = document.createElement("div");
        div.className = "theme-btn";
        div.style.cssText = `background: ${theme.background}; width: 25px; height: 25px`;
        btnContainer.appendChild(div);
        div.addEventListener("click", () => this.setTheme(theme));
      });
    }
  }
};
</script>






  
  <style>
  :root {
      --background: #1a1a2e;
      --color: #ffffff;
      --primary-color: #0f3460;
  }
  
  * {
      box-sizing: border-box;
  }
  
  html {
      scroll-behavior: smooth;
  }
  
  body {
      margin: 0;
      box-sizing: border-box;
      font-family: "poppins";
      background: var(--background);
      color: var(--color);
      letter-spacing: 1px;
      transition: background 0.2s ease, color 0.2s ease;
      -webkit-transition: background 0.2s ease, color 0.2s ease;
      -moz-transition: background 0.2s ease, color 0.2s ease;
      -ms-transition: background 0.2s ease, color 0.2s ease;
      -o-transition: background 0.2s ease, color 0.2s ease;
  }
  
  .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
      background: var(--background);
      color: var(--color);
      border-radius: 10px;
      box-shadow: 0 0 36px 1px rgba(0, 0, 0, 0.2);
      backdrop-filter: blur(20px);
  }
  
  .title {
      font-size: 2rem;
      margin-bottom: 1rem;
      color: var(--color);
  }
  
  .category {
      font-size: 1.2rem;
      margin-bottom: 2rem;
      color: var(--color);
  }
  
  .answers-heading,
  .add-answer-heading {
      font-size: 1.5rem;
      margin-bottom: 1rem;
      color: var(--color);
  }
  
  .answers-list {
      width: 100%;
      list-style: none;
      padding: 0;
      margin: 0;
      color: var(--color);
  }
  
  .answer-item {
      background: var(--primary-color);
      padding: 1rem;
      border-radius: 10px;
      margin-bottom: 1rem;
      transition: all 0.2s ease;
      color: var(--color);
  }
  
  .answer-item:hover {
      background: rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }
  
  .answer-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1rem;
      color: var(--color);
  }
  
  .like-count {
      font-size: 1.2rem;
      color: var(--color);
  }
  
  .smiley {
      cursor: pointer;
      font-size: 1.5rem;
      transition: all 0.2s ease;
      color: var(--color);
  }
  
  .smiley:hover {
      transform: scale(1.2);
  }
  
  .answer-form {
      width: 100%;
      max-width: 600px;
      margin-top: 2rem;
  }
  
  .form {
      display: flex;
      flex-direction: column;
  }
  
  .form-group {
      margin-bottom: 1rem;
  }
  
  .label {
      font-size: 1rem;
      margin-bottom: 0.5rem;
      color: var(--color);
  }
  
  .input {
      padding: 0.5rem;
      border: none;
      border-radius: 5px;
      outline: none;
      color: var(--color);
      background-color: rgba(255, 255, 255, 0.1);
  }
  
  .submit-button {
      background-color: var(--primary-color);
      color: var(--color);
      padding: 0.5rem;
      border-radius: 5px;
      border: none;
      cursor: pointer;
      transition: all 0.2s ease;
  }
  
  .submit-button:hover {
      background: rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }
  
  .theme-btn-container {
      position: absolute;
      left: 0;
      bottom: 2rem;
  }
  
  .theme-btn {
      cursor: pointer;
      transition: all 0.3s ease-in;
  }
  
  .theme-btn:hover {
      width: 40px !important;
  }
  
  @keyframes wobble {
      0% {
          transform: scale(1.025);
          -webkit-transform: scale(1.025);
          -moz-transform: scale(1.025);
          -ms-transform: scale(1.025);
          -o-transform: scale(1.025);
      }
      25% {
          transform: scale(1);
          -webkit-transform: scale(1);
          -moz-transform: scale(1);
          -ms-transform: scale(1);
          -o-transform: scale(1);
      }
      75% {
          transform: scale(1.025);
          -webkit-transform: scale(1.025);
          -moz-transform: scale(1.025);
          -ms-transform: scale(1.025);
          -o-transform: scale(1.025);
      }
      100% {
          transform: scale(1);
          -webkit-transform: scale(1);
          -moz-transform: scale(1);
          -ms-transform: scale(1);
          -o-transform: scale(1);
      }
  }
  </style>
  
  
  
  
  