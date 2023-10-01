<template>
  <div>
    <v-row align="center" justify="center" class="mt-1 mb-0">
      <h3>Overview of {{ $props.selectedCategory }} Companies</h3>
    </v-row>
    <div style="height: 90vh">
      <div id='myScatterPlot' style="height: inherit"></div>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "ScatterPlot",
  props: [
    "selectedCategory"
  ],
  data: () => ({
    ScatterPlotData: { x: [], y: [], name: [], category: [], color: [] },
    categoryColors: {
      tech: '#66c2a5',
      health: '#fc8d62',
      bank: '#8da0cb',
    }
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      // req URL to retrieve companies from backend
      var reqUrl = 'http://127.0.0.1:5000/companies?category=' + this.$props.selectedCategory
      console.log('ReqURL ' + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();

      // transform data to usable by scatterplot
      responseData.forEach((company) => {
        this.ScatterPlotData.name.push(company.name)
        this.ScatterPlotData.x.push(company.founding_year)
        this.ScatterPlotData.y.push(company.employees)
        this.ScatterPlotData.category.push(company.category)
        this.ScatterPlotData.color.push(this.categoryColors[company.category] || '#000');
      })
      console.log(this.ScatterPlotData)
      // after the data is loaded, draw the plot
      this.drawScatterPlot()
    },
    drawScatterPlot() {
      var trace1 = {
        x: this.ScatterPlotData.x,
        y: this.ScatterPlotData.y,
        mode: 'markers',
        type: 'scatter',
        text: this.ScatterPlotData.name,
        marker: {
          color: this.ScatterPlotData.color,
          size: 12
        }
      };
      var data = [trace1];
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
            text: 'Employees',
            font: {
              size: 18,
              color: '#7f7f7f'
            }
          }
        }
      }
      var config = { responsive: true, displayModeBar: false }
      Plotly.newPlot('myScatterPlot', data, layout, config);
      this.clickScatterPlot()
    },
    clickScatterPlot() {
      var pn = 0
      var that = this
      var myPlot = document.getElementById('myScatterPlot')
      myPlot.on('plotly_click', function (data) {
        for (var i = 0; i < data.points.length; i++) {

          // get the index of point
          pn = data.points[i].pointNumber;

          // emit event to change the currently selected company in the a) configuration panel
          // and b) update the Profit View
          that.$emit('changeCurrentlySelectedCompany', pn + 1)

          // revert all colors
          var colors = ['#00000' * 15]

          // and change currently selected color to blue
          colors[pn] = '#3777ee';

          // update the marker and plot
          var update = { 'marker': { color: colors, size: 12 } };
          Plotly.restyle('myScatterPlot', update);
        }
      });
    }

  },
  watch: {
    selectedCategory: function () {
      this.ScatterPlotData.x = [];
      this.ScatterPlotData.y = [];
      this.ScatterPlotData.name = [];
      this.ScatterPlotData.category = [];
      this.ScatterPlotData.color = [];

      this.fetchData();
    }
  }
}
</script>
