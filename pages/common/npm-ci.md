# npm ci

> Perform a clean install of a project.
> Designed for automated environments like CI/CD pipelines.
> More information: <https://docs.npmjs.com/cli/npm-ci>.

- Clean install a project-  Installs dependencies based on an existing `package-lock.json` or `npm-shrinkwrap.json`:

`npm ci`

- Exit with an error if dependencies don't match-  Will not update the `package-lock.json` if discrepancies are found:

`npm ci`

- Remove existing `node_modules` directory-  Automatically deletes the `node_modules` before installation:

`npm ci`

- Prevent modifications to `package.json`-  Ensures no changes are made to `package.json` or lock files during installation:

`npm ci`

- Set install strategy-  Adjusts how packages are installed in `node_modules`:

`npm config set install-strategy={{hoisted|nested|shallow|linked}}`
