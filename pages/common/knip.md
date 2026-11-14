# knip

> Find unused files, dependencies, and exports in JavaScript and TypeScript projects.
> More information: <https://knip.dev/reference/cli>.

- Analyze the current project for unused files, dependencies, and exports:

`knip`

- Run analysis in production mode, checking only production entry points and dependencies:

`knip --production`

- Automatically remove unused exports and dependencies where safe:

`knip --fix`

- Analyze a specific workspace in a monorepo:

`knip --workspace {{packages/app}}`
