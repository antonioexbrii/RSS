<template>
  <v-layout>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        placeholder="Refresh Rate (min.)"
        v-model="refreshrate"
        required
      ></v-text-field>
    </v-form>
  </v-layout>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped></style>
