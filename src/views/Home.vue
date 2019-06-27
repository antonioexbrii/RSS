<template>
  <div>
    <Stats v-bind:count="this.rssList.count" />
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
      labelList: [],
      yAxis: [],
      tf: [],
      idf: []
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
    }
  },
  created() {
    this.extractWords();
  }
};
</script>

<style lang="scss" scoped></style>
