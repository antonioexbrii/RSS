<template>
  <v-layout justify-space-around class="ma-3">
    <v-flex sm3>
      <v-card class="ma-2">
        <v-card-title class="justify-center">
          <div class="display-3">{{ ncount }}</div>
        </v-card-title>
        <v-card-text>
          <div class="display-1"># de notícias analisadas</div>
        </v-card-text>
      </v-card>
    </v-flex>
    <v-flex sm3>
      <v-card class="ma-2">
        <v-card-title class="justify-center">
          <div class="display-3">{{ wcount }}</div>
        </v-card-title>
        <v-card-text>
          <div class="display-1"># de palavras analisadas</div>
        </v-card-text>
      </v-card>
    </v-flex>
    <v-flex sm3>
      <v-card class="ma-2">
        <v-card-title class="justify-center">
          <div class="display-3">"{{ mrep.word }}"</div>
        </v-card-title>
        <v-card-text>
          <div class="display-1">palavra mais repetida ({{ mrep.count }}x)</div>
        </v-card-text>
      </v-card>
    </v-flex>
    <v-flex sm3>
      <v-card class="ma-2">
        <v-card-title class="justify-center">
          <div class="display-3">"{{ mrel.word }}"</div>
        </v-card-title>
        <v-card-text>
          <div class="display-1">
            palavra mais relevante ({{ mrel.tf * mrel.idf }})
          </div>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: {
    ncount: Number,
    wcount: Number,
    mrep: Object,
    mrel: Object
  }
};
</script>

<style lang="scss" scoped></style>
