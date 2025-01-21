<template>
  <div class="container">
    <div class="form-container">
      <h2 class="form-title">Add Question</h2>
      <Form @submit="submitQuestion" class="form" method="POST">
        <div class="form-group">
          <label for="question" class="form-label">Question</label>
          <Field name="question" type="text" id="question" placeholder="Enter your question" v-model="question"  class="form-input" />
          <ErrorMessage name="question" class="error-message" />
        </div>
        <div class="form-group">
          <label for="category" class="form-label">Choose a category:</label>
          <Field name="category" as="select" id="category"  class="form-select">
            <!-- <option value="" disabled>Select a category</option> -->
            <option v-for="categ in category" :key="categ.id" :value="categ.id" placeholder="Select a category">{{ categ.name }}</option>
          </Field>
          <ErrorMessage name="category" class="error-message" />
        </div>
        <button type="submit" class="submit-button">Save</button>
      </Form>
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from 'vee-validate';
import { mapState, mapActions } from 'vuex';

export default {
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    return {
      question: '',
      // category: '',
    };
  },
  computed: {
    ...mapState(['category']),
  },
  methods: {
    ...mapActions(['add_question','get_all_category']),
    submitQuestion(obj) {
      console.log(obj);
      this.add_question(obj)
      this.$router.push('/home');

  
      
      // this.add_question(formData)
      //   .then(() => {
      //     this.$router.push('/home');
      //   })
      //   .catch((error) => {
      //     console.error('Error adding question:', error);
      //   });
    },
  },

  mounted(){
    this.get_all_category()
  }

};
</script>

]


<style scoped>
:root {
    --background: #1a1a2e;
    --color: #ffffff;
    --primary-color: #0f3460;
    --error-color: #ff6b6b;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: "Poppins", sans-serif;
    background: var(--background);
    color: var(--color);
    letter-spacing: 1px;
    transition: background 0.2s ease, color 0.2s ease;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    height:100vh;
    padding: 2rem;
    min-width: 200vh;
}

.form-container {
    border: 1px solid hsla(0, 0%, 65%, 0.158);
    box-shadow: 0 0 36px 1px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    backdrop-filter: blur(20px);
    padding: 2rem;
    width: 100%;
    max-width: 600px;
    background: var(--background);
    color: var(--color);
}

.form-title {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: var(--color);
}

.form {
    display: flex;
    flex-direction: column;
}

.form-group {
    margin-bottom: 1rem;
}

.form-label {
    font-size: 1rem;
    margin-bottom: 0.5rem;
    color: var(--color);
}

.form-input,
.form-select {
    padding: 0.5rem;
    border: none;
    border-radius: 5px;
    outline: none;
    color: var(--color);
    background-color: rgba(255, 255, 255, 0.1);
    width: 100%;
}

.form-input::placeholder,
.form-select::placeholder {
    color: var(--color);
    opacity: 0.7;
}

.error-message {
    color: var(--error-color);
    font-size: 0.875rem;
    margin-top: 0.5rem;
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
</style>

  