# knip

> Find unused files, dependencies, and exports in JavaScript and TypeScript projects.
> More information: <https://knip.dev/reference/cli>.

- Analyze the current project for unused files, dependencies, and exports:

`knip`

- Run analysis in production mode (ignoring test and development files):

`knip --production`

- Check only for unused dependencies:

`knip --dependencies`

- Check only for unused exports:

`knip --exports`

- Automatically remove unused exports and dependencies where possible:

`knip --fix`
