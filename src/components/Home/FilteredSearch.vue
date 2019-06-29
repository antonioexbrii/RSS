<template>
  <div>
    <v-flex xs12 sm6 md3>
      <v-text-field
        v-model="searchTerm"
        label="Search by TFxIDF"
        outline
      ></v-text-field>
    </v-flex>
    <li>
      <ul v-for="word in filteredWords" v-bind:key="word.word">
        {{
          word.sentence
        }}
      </ul>
    </li>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      searchTerm: ""
    };
  },
  props: {
    algo: Array,
    deposit: Array
  },
  computed: {
    filteredWords: function() {
      var matcher = new RegExp(this.searchTerm, "i");
      return this.algo.filter(function(w) {
        return matcher.test(w.sentence);
      });
    }
  }
};
</script>

<style lang="scss" scoped></style>
