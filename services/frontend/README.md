# Frontend

Vue 3 app with Vuetify and Plotly.js, built with Vite. It shows the company dashboard and calls the Flask API at
`VITE_API_URL` (default `http://localhost:5001`, see [`src/api.js`](src/api.js)).

| File | Content |
|---|---|
| [`src/App.vue`](src/App.vue) | App bar and layout |
| [`src/components/ConfigurationPanel.vue`](src/components/ConfigurationPanel.vue) | Dropdowns for category, company and algorithm; holds the plots |
| [`src/components/ScatterPlot.vue`](src/components/ScatterPlot.vue) | Founding year vs. employees; a click selects the company |
| [`src/components/LinePlot.vue`](src/components/LinePlot.vue) | Profit per year with the predicted value in red |
| [`src/components/BarPlot.vue`](src/components/BarPlot.vue) | Employees of the companies in the category of the selected company |

## Commands

```bash
npm ci
```

```bash
npm run dev
```

```bash
npm run lint
```

```bash
npm run build
```

The dev server runs on <http://localhost:8080>. In Docker, the [`Dockerfile`](Dockerfile) builds the app and serves it
with nginx.
