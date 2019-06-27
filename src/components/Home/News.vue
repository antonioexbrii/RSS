<template>
  <v-data-table
    :headers="this.cabec"
    :items="this.newsList"
    class="elevation-1"
  >
    <template v-slot:items="props">
      <tr>
        <td>{{ props.item.title }}</td>
      </tr>
    </template>
  </v-data-table>
</template>

<script>
export default {
  data: () => ({
    cabec: [{ text: "Title", value: "title" }]
  }),
  props: {
    newsList: Array
  }
};
</script>

<style lang="scss" scoped></style>
