<script>
import { Doughnut } from "vue-chartjs";
export default {
  extends: Doughnut,
  props: {
    lbs: Array,
    yaxis: Array
  },
  data() {
    return {
      datacollection: {
        labels: this.lbs,
        datasets: [
          {
            backgroundColor: [
              "#41B883",
              "#E46651",
              "#00D8FF",
              "#DD1B16",
              "#f55a42",
              "#cca43f",
              "#455c24",
              "#296652",
              "#275ecc",
              "#5e27ab",
              "#8b13a1",
              "#9e0b37",
              "#146e48",
              "#53e653",
              "#28a9b8",
              "#113e82",
              "#ffe600",
              "#b979d9",
              "#d938be"
            ],
            data: this.yaxis
          }
        ]
      },
      options: { responsive: true, maintainAspectRatio: false }
    };
  },
  mounted() {
    this.renderChart(this.datacollection, this.options);
  },
  watch: {
    lbs() {
      this.datacollection.labels = this.lbs;
      this.datacollection.datasets[0].data = this.yaxis;

      this.renderChart(this.datacollection, this.options);
    }
  }
};
</script>
