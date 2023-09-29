<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-container fluid>
        <v-row justify="center">
          <v-col>
            <h2 class="text-h2">Nicolas Huber - 16-936-205</h2>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>
    <v-main>
      <ConfigurationPanel />
    </v-main>
  </v-app>
</template>

<script>
import ConfigurationPanel from './components/ConfigurationPanel.vue'

export default {
  name: 'App',

  components: {
    ConfigurationPanel,
  },

  data: () => ({
    //
  }),
}
</script>

<style>
/* disable scrolling */
html {
  scrollbar-width: none;
  /* For Firefox */
  -ms-overflow-style: none;
  /* For Internet Explorer and Edge */
}

html::-webkit-scrollbar {
  width: 0px;
  /* For Chrome, Safari, and Opera */
}
h2 {
  text-align: center;
}
</style>