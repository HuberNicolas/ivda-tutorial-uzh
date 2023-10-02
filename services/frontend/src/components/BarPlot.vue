<template>
  <div>
    <v-row align="center" justify="center" class="mt-1 mb-0">
      <h3 v-if="selectedCompanyData">Employees per Company in the {{ selectedCompanyData.category }} Category</h3>
    </v-row>
    <div style="height: 90vh">
      <div id='myBarPlot' style="height: inherit"></div>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "BarPlot",
  props: ["selectedCompany"],
  data: () => ({
    BarPlotData: { x: [], y: [] },
    selectedCompanyData: null,
    selectedCategory: ''
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      // req URL to retrieve single company from backend
      var reqUrl = 'http://127.0.0.1:5000/companies'
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();

      this.selectedCompanyData = responseData.find((company) => company.id === this.$props.selectedCompany);
      this.selectedCategory = this.selectedCompanyData.category;


      // transform data to usable by barplot
      responseData.forEach((company) => {
        if (company.category === this.selectedCategory) {
          this.BarPlotData.x.push(company.name)
          this.BarPlotData.y.push(company.employees)
        }
      })

      // draw the barplot after the data is transformed
      this.drawBarPlot()
    },
    drawBarPlot() {
      var data = [];
      data = [{
        x: this.BarPlotData.x,
        y: this.BarPlotData.y,
        name: 'Employees per Company in' + this.selectedCategory,
        type: 'bar'
      }];

      var layout = {
        xaxis: {
          title: {
            text: 'Employees',
            font: {
              size: 18,
              color: '#7f7f7f'
            }
          },
        },
        yaxis: {
          title: {
            text: 'Company',
            font: {
              size: 18,
              color: '#7f7f7f'
            }
          }
        }
      }
      var config = { responsive: true, displayModeBar: false }
      Plotly.newPlot('myBarPlot', data, layout, config);
    }
  },
  watch: {
    selectedCompany() {
      this.LinePlotData.x = [];
      this.LinePlotData.y = [];
      this.fetchData();
    },
  },
}
</script>
