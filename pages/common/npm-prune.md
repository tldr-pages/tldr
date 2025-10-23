# npm-prune

> Remove extraneous packages from `node_modules` that are not listed in `package.json`.
> Helps keep dependencies tidy.
> More information: <https://docs.npmjs.com/cli/npm-prune>.

- Remove unlisted packages from `node_modules`:

`npm prune`

- Remove unlisted packages, including those installed with `--production`:

`npm prune --production`

- Simulate the removal process without making changes:

`npm prune --dry-run`
