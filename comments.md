# Part 0
- Use the Default option (Vuetify for Vue 3) and press enter.
  - for me that is not very clear, since the default option seems to be the first option "Vuetify 2 - Configure Vue CLI (advanced)" or even "Vuetify 2 - Vue CLI (recommended)"

# Part 1
- There is no existing styling in App.vue
- Small typo (App.Vue instead of App.vue)
- Renaming "HelloWorld.vue" Component to "ConfigurationPanel.vue" did not break the code for me
- Color is not quite correct

# Part 2
- Could install plotly w/o root
- Small: After installing, it is not indicated to start the server again
- Maybe not use inline styles (I'm not a Vue-expert)
- Maybe directly load data from an .json file instead of placing in into the Code section
- Maybe provide simple Vue template
- Maybe start server with hot reloading: "npm run serve --hot"

# Part 3
- It is a bit cumbersome to copy all of it again
- Maybe explicitly show and explain, how to select an env
- Maybe mention the difference of the source command and selecting an env in PyCharm
- Mention Flask and Werkzeug conflict

# Part 4
- Maybe use docker instead of installing mongo and mongo-express
- It is not companies.json but main_company.json
- Maybe mention that we could also use something like sqlite?

# Part 5
- Not sure if we should keep the v-card

# Part 6
- Mention separation of imports (e.g., request)
- Mention cors error (better use Chrome)

# Part 7
- Async fetchData() is a '}' missing

# Part 9
- What do you mean sidebar? "Make a decision on the design that visually highlights the configuration panel."

# Additional Feedback
- It would be nice to have some part of the tutorial regarding Vue styling; most useful would I find a short section about the management of the components: How do I divide the screen into meaningful parts (e.g., command- vs. plotarea)
- Maybe we could dockerize everything?
- It would be nice to have a short introduction to Postman: It would speed up the development between the Front- and Backend-teams
- We used SQLite as DB. Maybe just include a link to other DB systems.