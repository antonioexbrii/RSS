<template>
  <div>
    <Stats v-bind:ncount="this.rssList.count" v-bind:wcount="this.totalWords" />
    <v-divider></v-divider>
    <News v-bind:newsList="this.rssList.entries" @fclick="extractWords" />
    <Graphs
      v-bind:yAxis.sync="this.yAxis"
      v-bind:labArray.sync="this.labelList"
      v-bind:tfArray.sync="this.tf"
      v-bind:idfArray.sync="this.idf"
    />
    <DNGraph v-bind:lbs="this.labelList" v-bind:yaxis="this.tf" />
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
      totalWords: 0
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
        console.log(value);
        for (w = 0; w < this.algoData.collection.length; w++) {
          console.log(this.algoData.collection[w].sentence);
          if (value === this.algoData.collection[w].sentence) {
            w = n;
            console.log(w);
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

<style lang="scss" scoped></style>
