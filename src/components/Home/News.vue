<template>
  <v-layout>
    <v-flex sm10 offset-sm1 text-xs-center>
      <div class="display-2">Notícias mais recentes</div>
      <v-sheet>
        <v-card class="mt-2" v-for="n in 5" :key="n">
          <v-card-title>
            <div class="headline">Título da Notícia {{ n }}</div>
          </v-card-title>
          <v-divider></v-divider>
        </v-card>
      </v-sheet>
    </v-flex>
  </v-layout>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped></style>
