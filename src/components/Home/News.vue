<template>
  <v-container>
    <v-sheet color="grey lighten-3" :key="{ n }" v-for="n in 3">
      <div class="headline">Título da notícia</div>
    </v-sheet>
  </v-container>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped></style>
