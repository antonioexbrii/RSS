<template>
  <v-app>
    <v-tabs
      fixed-tabs
      centered
      v-model="active"
      color="cyan"
      dark
      slider-color="yellow"
    >
      <v-tab :key="feed">Feed</v-tab>
      <v-tab :key="configuration">Configuration</v-tab>
      <v-tab :key="about">About</v-tab>
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
