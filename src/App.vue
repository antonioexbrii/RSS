<template>
  <v-app class="d1">
    <v-tabs fixed-tabs centered color="#152e8a" dark slider-color="yellow">
      <v-tab :key="feed">Feed</v-tab>
      <v-tab :key="configuration">Configuração</v-tab>
      <v-tab :key="about">Sobre</v-tab>
      <v-tab-item :key="feed">
        <Home />
      </v-tab-item>
      <v-tab-item :key="configuration">
        <Configuration />
      </v-tab-item>
      <v-tab-item :key="about">
        <About />
      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
import Home from "@/views/Home";
import Configuration from "@/views/Configuration";
import About from "@/views/About";

export default {
  name: "App",
  components: {
    Home,
    Configuration,
    About
  },
  data() {
    return {
      //
    };
  }
};
</script>
<style scoped>
.d1 {
  background-color: cornflowerblue;
}
</style>
