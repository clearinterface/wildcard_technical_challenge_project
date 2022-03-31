<template>
  <div class="container">
  <div class="row">
<p class="bg-primary">...</p>
    <form v-on:submit.prevent="submitForm">
  <div class="field">
    <div class="form-control">
                <label class="label">Censored words or phrases: </label>
    </div>
    <div class="form-control">
          <input class="input" size="90" type="text" placeholder="Text input" id="filtered_words" v-model="filtered_words">
    </div>
    <p></p>
        <div class="form-control">
                    <label class="label">Text to filter: </label>

        </div>
        <div class="form-control">
          <textarea class="input" cols="90" rows="5" id="document_text" v-model="document_text"></textarea>
    </div>
    <div class="form-control">
         <button type="submit">Submit</button>
    </div>
  </div>
    </form>


        <p class="lead">{{ censored_text }}</p>
</div>

  </div>





</template>

<script>
export default {
    data(){
    return {
        censored_text: '',
        filtered_words: '',
        document_text: ''
    }
},

  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods:{
    async submitForm(){
      try {
        // Send a POST request to the API
        const response = await this.$http.post('http://127.0.0.1:8000/api/words/', {
            filtered_words: this.filtered_words,
            document_text: this.document_text,
            completed: false
        });
        // Append the returned data to the tasks array
        //this.tasks.push(response.data);
        this.censored_text = response.data['censored_text']
        // Reset the title and description field values.
        //this.filtered_words = '';
        //this.document_text = '';
    } catch (error) {
        // Log the error
        console.log(error);
    }
    }
  },


}




</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
