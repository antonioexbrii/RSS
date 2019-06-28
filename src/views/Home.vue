<template>
  <div class="d1">
    <Stats v-bind:ncount="this.rssList.count" v-bind:wcount="this.totalWords" />
    <v-flex sm8 offset-sm2>
      <News v-bind:newsList="this.rssList.entries" @fclick="extractWords" />
    </v-flex>
    <v-sheet>
      <v-layout class="ma-3">
        <v-flex sm5 offset-sm1>
          <Graphs
            v-bind:update.sync="this.up"
            v-bind:yAxis.sync="this.yAxis"
            v-bind:labArray.sync="this.labelList"
            v-bind:tfArray.sync="this.tf"
            v-bind:idfArray.sync="this.idf"
          />
        </v-flex>
        <v-flex sm5>
          <DNGraph v-bind:lbs="this.labelList" v-bind:yaxis="this.tf" />
        </v-flex>
      </v-layout>
    </v-sheet>
  </div>
</template>

<script>
import Stats from "@/components/Home/Stats";
import News from "@/components/Home/News";
import Graphs from "@/components/Home/Graphs";
import DNGraph from "@/components/Home/DNGraph";
import rss from "../../public/algorithm/rssnews.json";
import algo from "../../public/algorithm/algorithm.json";
import depo from "../../public/algorithm/deposit.json";
export default {
  components: {
    Stats,
    News,
    Graphs,
    DNGraph
  },
  data() {
    return {
      rssList: rss,
      algoData: algo,
      depositInfo: depo,
      labelList: [],
      yAxis: [],
      tf: [],
      idf: [],
      totalWords: 0,
      up: true
    };
  },
  methods: {
    extractWords(value) {
      var labels = [];
      var ya = [];
      var tfl = [];
      var idfl = [];
      var w;
      var n = 0;
      if (value) {
        for (w = 0; w < this.algoData.collection.length; w++) {
          if (value === this.algoData.collection[w].sentence) {
            n = w;
          }
        }
      }
      for (w of this.algoData.collection[n].words) {
        labels.push(w.word);
        var nw = w.tf * w.idf;
        tfl.push(w.tf);
        idfl.push(w.idf);
        ya.push(nw);
      }
      this.labelList = labels;
      this.yAxis = ya;
      this.tf = tfl;
      this.idf = idfl;
    },
    numWords: function() {
      var ct = 0;
      var entry;
      for (entry of this.depositInfo.entries) {
        ct += entry.count;
      }
      this.totalWords = ct;
    }
  },
  created() {
    this.extractWords("not");
    this.numWords();
  }
};
</script>

<style scoped>
.d1 {
  background-color: azure;
}
</style>
