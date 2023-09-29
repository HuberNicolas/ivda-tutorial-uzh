// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

// Vuetify
import { createVuetify } from "vuetify";
import colors from "vuetify/lib/util/colors";

export default createVuetify({
  // https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
  theme: {
    themes: {
      light: {
        dark: false,
        colors: {
          // https://vuetifyjs.com/en/styles/colors/#material-colors
          primary: colors.blue.darken3,
          secondary: colors.blue.accent2,
        },
      },
    },
  },
});
