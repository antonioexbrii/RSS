<template>
  <div>
    <Stats />
    <News />
    <Graphs />
  </div>
</template>

<script>
import Stats from "@/components/Home/Stats";
import News from "@/components/Home/News";
import Graphs from "@/components/Home/Graphs";
export default {
  components: {
    Stats,
    News,
    Graphs
  }
};
</script>

<style lang="scss" scoped></style>
