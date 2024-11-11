# npm ci

> Clean install of `npm` project dependencies to be used in automated environments.
> Installs packages based on `package-lock.json` or `npm-shrinkwrap.json`.
> More information: <https://docs.npmjs.com/cli/commands/npm-ci>.

- Install project dependencies from `package-lock.json` or `npm-shrinkwrap.json`:

`npm ci`

- Install project dependencies but skip the specified packages:

`npm ci --omit={{dev|optional|peer}}`

- Install project dependencies without running any pre- or post-scripts defined in `package.json`:

`npm ci --ignore-scripts`
