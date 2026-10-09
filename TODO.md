# TODO

Open tasks before the repository is made public. See also [Known issues](README.md#known-issues).

## 1. Version 1 (state of October 2023)

- [x] Tag `v1.0.0` on the last commit from 2023 (`Comments`, 5 October 2023)
- [ ] Push the tag and create a GitHub release with the course context

## 2. Version 2

- [x] Compose: pinned images, own network, health check, backend and frontend services, mongo-express as profile
- [x] Backend: Flask 3, Pydantic 2, uv lockfile, `MONGO_URI`, gunicorn, Ruff
- [x] Frontend: Vite, stable Vuetify, `VITE_API_URL`, ESLint flat config
- [x] Fix scatter plot selection, scatter colours and bar plot crash
- [x] Test the full stack in Docker (API calls, dashboard in the browser, mongo-express login)
- [ ] Tag `v2.0.0` after the first green CI run on GitHub

## 3. Before publishing

- [x] Rename the repository to `ivda-tutorial-uzh` (`2023` only in the README)
- [x] License: MIT for my code, MPL-2.0 for the tutorial material
- [x] Add the context (course, UZH, IVDA group, Prof. Dr. Jürgen Bernard, my role) to the README
- [x] Credit the IVDA group for the tutorial, screenshots and mock data
- [ ] Confirm with the IVDA group that the tutorial material may stay public in this repository
- [x] Check for secrets in the files and the git history (only local default passwords for mongo-express)
- [ ] Rewrite the old UZH e-mail in the commit metadata, then force-push
