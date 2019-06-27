<template>
  <v-layout>
    <v-flex sm10 offset-sm1 text-xs-center>
      <div class="display-2">Notícias mais recentes</div>
      <v-sheet>
        <v-card class="mt-2" v-for="n in allNews.entries" :key="n.link">
          <v-card-title>
            <div class="headline">{{ n.title }}</div>
          </v-card-title>
          <v-divider></v-divider>
        </v-card>
      </v-sheet>
    </v-flex>
  </v-layout>
</template>

<script>
import rssnews from "../../../public/algorithm/rssnews.json";
export default {
  data() {
    return {
      allNews: rssnews
    };
  },
  methods: {
    refreshNews: function() {
      import("../../../public/algorithm/rssnews.json").then(m => {
        this.allNews = m;
      });
    }
  }
};
</script>

<style lang="scss" scoped></style>
