<script>
import { Bar } from "vue-chartjs";
export default {
  extends: Bar,
  props: {
    labArray: Array,
    yAxis: Array,
    tfArray: Array,
    idfArray: Array
  },
  data() {
    return {
      datacollection: {
        labels: this.labArray,
        datasets: [
          {
            label: "TF x IDF",
            backgroundColor: "#f87979",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: this.yAxis
          },
          {
            label: "TF",
            backgroundColor: "#4287f5",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: this.tfArray
          },
          {
            label: "IDF",
            backgroundColor: "#9370db",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: this.idfArray
          }
        ]
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }
          ],
          xAxes: [
            {
              gridLines: {
                display: false
              }
            }
          ]
        },
        legend: {
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  mounted() {
    this.renderChart(this.datacollection, this.options);
  }
};
</script>
