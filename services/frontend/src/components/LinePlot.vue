<template>
  <div>
    <v-row align="center" justify="center" class="mt-1 mb-0">
      <h3>Profit View of Company: {{ $props.selectedCompany }}</h3>
    </v-row>
    <div style="height: 90vh">
      <div id='myLinePlot' style="height: inherit"></div>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "LinePlot",
  props: ["selectedCompany", "selectedAlgorithm"],
  data: () => ({
    LinePlotData: { x: [], y: [] }
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      // req URL to retrieve single company from backend
      var reqUrl = 'http://127.0.0.1:5000/companies/' + this.$props.selectedCompany +
        '?algorithm=' + this.$props.selectedAlgorithm
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      // transform data to usable by lineplot
      responseData.profit.forEach((profit) => {
        this.LinePlotData.x.push(profit.year)
        this.LinePlotData.y.push(profit.value)
      })
      // draw the lineplot after the data is transformed
      this.drawLinePlot()
    },
    drawLinePlot() {
      var data = [];

      // Check if the selected algorithm is 'none'
      if (this.selectedAlgorithm === "none") {
        
        data = [{
          x: this.LinePlotData.x,
          y: this.LinePlotData.y,
          name: 'Profit per Year',
          type: 'scatter'
        }];
      } else {
        // Add a scatter plot with markers for all points except the last one
        data.push({
          x: this.LinePlotData.x.slice(1), // Exclude the first and second point
          y: this.LinePlotData.y.slice(1), // Exclude the first and second point
          name: 'Profit per Year',
          type: 'scatter',
          mode: 'lines+markers',
          line: {
            width: 2,
          },
          marker: {
            size: 6,
          }
        });

        // Add the last 2 points with special formatting (line and marker)
        data.push({
          x: this.LinePlotData.x.slice(0,2), // Last and second last points
          y: this.LinePlotData.y.slice(0,2), // Last and second last points
          name: 'Predicted Profit Year',
          type: 'scatter',
          mode: 'lines+markers',
          line: {
            width: 2,
            color: 'red', // Line color for the last point
            dash: 'dot'
          },
          marker: {
            size: 10,
            color: 'red' // Marker color for the last point
          }
        });
        
      }

      var layout = {
        xaxis: {
          title: {
            text: 'Year',
            font: {
              size: 18,
              color: '#7f7f7f'
            }
          },
        },
        yaxis: {
          title: {
            text: 'Profit',
            font: {
              size: 18,
              color: '#7f7f7f'
            }
          }
        }
      }
      var config = { responsive: true, displayModeBar: false }
      Plotly.newPlot('myLinePlot', data, layout, config);
    }
  },
  watch: {
    selectedCompany() {
      this.LinePlotData.x = [];
      this.LinePlotData.y = [];

      this.fetchData();
    },
    selectedAlgorithm() {
      this.LinePlotData.x = [];
      this.LinePlotData.y = [];

      this.fetchData();
    }
  },
}
</script>
