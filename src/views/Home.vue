<template>
  <div>
    <Stats
      v-bind:ncount="this.rssList.count"
      v-bind:wcount="this.totalWords"
      v-bind:mrep="this.mostRepetitions"
      v-bind:mrel="this.mostRelevant"
    />

    <v-sheet class="pa-2 mt-2 mb-2">
      <v-layout>
        <v-flex sm7 xs12>
          <v-card flat>
            <v-card-title class="justify-center">
              <div class="display-2">Lista de notícias do feed RSS</div>
            </v-card-title>
            <News
              v-bind:newsList="this.rssList.entries"
              @fclick="extractWords"
            />
          </v-card>
        </v-flex>
        <v-flex sm5 xs12>
          <v-card flat>
            <v-card-title class="justify-center">
              <div class="display-2 justify-center">
                O que é o TF-IDF?
              </div> 
              </v-card-title>
              <v-img :src="require('../assets/equation.png')" contain height="200" ></v-img>
            <v-card-text>
              <div class="body1">
                O valor tf–idf (abreviação do inglês term frequency–inverse
                document frequency, que significa frequência do termo–inverso da
                frequência nos documentos), é uma medida estatística que tem o
                intuito de indicar a importância de uma palavra de um documento
                em relação a uma coleção de documentos ou em um corpus
                linguístico. Ela é frequentemente utilizada como fator de
                ponderação na recuperação de informações e na mineração de
                dados. O valor tf–idf de uma palavra aumenta proporcionalmente à
                medida que aumenta o número de ocorrências dela em um documento,
                no entanto, esse valor é equilibrado pela frequência da palavra
                no corpus.
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-sheet>
    <v-sheet class="pa-2 mt-2 mb-2">
      <v-flex sm8 offset-sm2>
        <v-card flat class="ma-2 pa-2">
          <v-card-title class="justify-center">
            <div class="display-2">Resultados do Algoritmo</div>
          </v-card-title>
          <Graphs
            v-bind:yAxis.sync="this.yAxis"
            v-bind:labArray.sync="this.labelList"
            v-bind:tfArray.sync="this.tf"
            v-bind:idfArray.sync="this.idf"
          />
        </v-card>
      </v-flex>
    </v-sheet>
    <v-sheet class="pa-2 mt-2 mb-2">
      <v-flex sm8 offset-sm2>
        <v-card flat class="ma-2 pa-2">
          <v-card-title class="justify-center">
            <div class="display-2">Frequência de Termo da Frase</div>
          </v-card-title>
          <DNGraph v-bind:lbs="this.labelList" v-bind:yaxis="this.tf" />
        </v-card>
      </v-flex>
    </v-sheet>
    <v-sheet class="pa-2 mt-2 mb-2">
      <v-flex sm8 offset-sm2>
        <v-card flat class="ma-2 pa-2">
          <v-card-title class="justify-center">
            <div class="display-2">Procura de palavras</div>
          </v-card-title>
          <FilteredSearch
            v-bind:algo="this.algoData.collection"
            v-bind:deposit="this.depositInfo.entries"
          />
        </v-card>
      </v-flex>
    </v-sheet>
  </div>
</template>

<script>
import Stats from "@/components/Home/Stats";
import News from "@/components/Home/News";
import Graphs from "@/components/Home/Graphs";
import DNGraph from "@/components/Home/DNGraph";
import FilteredSearch from "@/components/Home/FilteredSearch";
import rss from "../../public/algorithm/rssnews.json";
import algo from "../../public/algorithm/algorithm.json";
import depo from "../../public/algorithm/deposit.json";
export default {
  components: {
    Stats,
    News,
    Graphs,
    DNGraph,
    FilteredSearch
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
      allWords: {
        ww: []
      }
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
    },
    fillWords() {
      this.algoData.collection.map(entry => {
        entry.words.map(w => {
          this.allWords.ww.push(w);
        });
      });
    }
  },
  computed: {
    mostRepetitions() {
      return this.depositInfo.entries.reduce(function(max, x) {
        return x.count > max.count ? x : max;
      });
    },
    mostRelevant() {
      return this.allWords.ww.reduce(function(max, x) {
        return x.tf * x.idf > max.tf * max.idf ? x : max;
      });
    }
  },
  created() {
    this.extractWords("not");
    this.numWords();
    this.fillWords();
  }
};
</script>
