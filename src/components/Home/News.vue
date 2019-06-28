<template>
  <v-data-table
    :headers="this.cabec"
    :items="this.newsList"
    class="elevation-1"
  >
    <template v-slot:items="props">
      <tr @click="feedClick(props.item.sentence)">
        <td>{{ props.item.title }}</td>
        <td>{{ props.item.pubDate }}</td>
      </tr>
    </template>
  </v-data-table>
</template>

<script>
export default {
  data: () => ({
    cabec: [
      { text: "Title", value: "title" },
      { text: "Date", value: "pubDate" }
    ]
  }),
  props: {
    newsList: Array
  },
  methods: {
    feedClick: function(tit) {
      this.$emit("fclick", tit);
    }
  }
};
</script>

<style lang="scss" scoped></style>
