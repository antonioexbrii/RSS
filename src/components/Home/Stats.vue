<template>
  <v-layout justify-space-around class="ma-3">
    <v-flex class="ma-2">
      <v-card>
        <v-card-title class="justify-center">
          <div class="display-2">{{ count }}</div>
          <div class="display-1"># de Notícias analisadas</div>
        </v-card-title>
      </v-card>
    </v-flex>
    <v-flex class="ma-2">
      <v-card>
        <v-card-title class="justify-center">
          <div class="display-2">123</div>
          <div class="display-1"># de Palavras analisadas</div>
        </v-card-title>
      </v-card>
    </v-flex>
    <v-flex class="ma-2">
      <v-card>
        <v-card-title class="justify-center">
          <div class="display-2">123</div>
          <div class="display-1">Palavra mais relevante</div>
        </v-card-title>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: {
    count: Number
  }
};
</script>

<style lang="scss" scoped></style>
