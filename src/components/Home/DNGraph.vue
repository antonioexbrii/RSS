<script>
import { Doughnut } from "vue-chartjs";
export default {
  extends: Doughnut,
  props: {
    lbs: Array,
    yaxis: Array
  },
  mounted() {
    this.renderChart(
      {
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
              "#9e0b37"
            ],
            data: this.yaxis
          }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  }
};
</script>
