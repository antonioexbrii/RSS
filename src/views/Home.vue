<template>
  <div>
    <Stats v-bind:ncount="this.rssList.count" v-bind:wcount="this.totalWords" />
    <v-divider></v-divider>
    <News v-bind:newsList="this.rssList.entries" />
    <Graphs
      v-bind:yAxis="this.yAxis"
      v-bind:labArray="this.labelList"
      v-bind:tfArray="this.tf"
      v-bind:idfArray="this.idf"
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
    extractWords: function() {
      var labels = [];
      var ya = [];
      var tfl = [];
      var idfl = [];
      var w;
      for (w of this.algoData.collection[0].words) {
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
        console.log(entry.count);
        ct += entry.count;
      }
      this.totalWords = ct;
    }
  },
  created() {
    this.extractWords();
    this.numWords();
  }
};
</script>

<style lang="scss" scoped></style>
