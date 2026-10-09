<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="2" class="sideBar bg-blue-darken-3">
          <v-row>
            <v-col cols="12" sm="12">
              <div class="control-panel-font">Company Overview</div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" sm="12">
              <v-select :items="categories.values" label="Select a category" density="compact" v-model="categories.selectedValue"
                @update:model-value="changeCategory"></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" sm="12">
              <div class="control-panel-font">Profit View of Company</div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" sm="12">
              <v-select :items="companies.items" label="Select a company" density="compact" v-model="companies.selectedValue" item-title="name" item-value="id"
                @update:model-value="changeCompany"></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" sm="12">
              <v-select :items="algorithm.values" label="Select an algorithm for prediction" density="compact"
                v-model="algorithm.selectedValue" @update:model-value="changeAlgorithm"></v-select>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" md="5" class="plot-area bg-blue-accent-1">
          <ScatterPlot :key="scatterPlotId" :selectedCategory="categories.selectedValue"
            @changeCurrentlySelectedCompany="changeCurrentlySelectedCompany" />
          <BarPlot :key="barPlotId" :selectedCompany="companies.selectedValue" />
        </v-col>
        <v-col cols="12" md="5" class="plot-area bg-blue-accent-1">
          <LinePlot :key="linePlotId" :selectedCompany="companies.selectedValue"
            :selectedAlgorithm="algorithm.selectedValue" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import ScatterPlot from './ScatterPlot.vue';
import LinePlot from './LinePlot.vue';
import BarPlot from './BarPlot.vue';
import { API_URL } from '@/api';
export default {
  components: { ScatterPlot, LinePlot, BarPlot },
  data: () => ({
    scatterPlotId: 0,
    linePlotId: 1,
    barPlotId: 0,
    categories: {
      values: ['All', 'tech', 'health', 'bank'],
      selectedValue: 'All'
    },
    companies: {
      items: [],
      selectedValue: 1
    },
    algorithm: {
      values: ['none', 'random', 'regression'],
      selectedValue: 'none'
    }
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      // req URL to retrieve all companies from backend
      var reqUrl = API_URL + '/companies'
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      this.companies.items = responseData.map(company => ({
        // https://dev.vuetifyjs.com/en/api/v-select/
         id: company.id,
         name: company.name
      }));
    },
    changeCategory() {
      this.scatterPlotId += 1
    },
    changeCompany() {
      this.linePlotId += 1
      this.barPlotId += 1
    },
    changeAlgorithm() {
      this.linePlotId += 1
    },
    changeCurrentlySelectedCompany(companyId) {
      this.companies.selectedValue = companyId
      this.changeCompany()
    },
  }
}
</script>
<style scoped>
.control-panel-font {
  font-family: "Open Sans", verdana, arial, sans-serif;
  align-items: center;
  font-size: 15px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  display: flex;
  font-weight: 500;
  height: 40px;
}

.sideBar {
  height: calc(100vh - 50px);
}

.plot-area {
  height: calc(100vh - 50px);
}
</style>