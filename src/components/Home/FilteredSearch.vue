<template>
  <div>
    <v-flex xs12>
      <v-text-field
        full-width=true
        v-model="searchTerm"
        label="Search by TFxIDF"
        outline
      ></v-text-field>
    </v-flex>
    <v-list two-line>
      <template v-for="word in filteredWords">
        <v-list-tile :key="word.word">
          <v-list-tile-content>
            <v-list-tile-title v-html="word.title"></v-list-tile-title>
            <v-list-tile-sub-title>{{'(Σ tf-idf de palavras) / número de palavras: '+word.sentence_tfidf}}</v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>
    </v-list>
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
      if(this.searchTerm === "")
        return []
      var matcher = new RegExp(this.searchTerm, "i");
      return this.algo.filter(function(w) {
        return matcher.test(w.sentence);
      }).sort(function(a,b) {
        return b.sentence_tfidf - a.sentence_tfidf
      });
    }
  },
  methods: {
    calcWords: async function(words){
      var w
      var t = 0;
      for(w of words) {
        t += await w.tf * w.idf
      }
      t = await t/words.length
      return t
    }
  }
};
</script>

<style lang="scss" scoped></style>
