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
      }).sort(function(a,b) {
        var aw;
        var bw;
        var aRes=0;
        var bRes=0;
        for(aw of a.words)
          aRes += aw.tf * aw.idf
        aRes = aRes/a.words.length
        for(bw of b.words)
          bRes += bw.tf * bw.idf
        bRes = bRes/b.words.length
        return aRes - bRes
      });
    }
  }
};
</script>

<style lang="scss" scoped></style>
