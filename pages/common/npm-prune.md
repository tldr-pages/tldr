# npm prune

> Remove extraneous packages from `node_modules`.
> More information: <https://docs.npmjs.com/cli/commands/npm-prune>.

- Remove all extraneous packages not listed in dependencies:

`npm prune`

- Remove extraneous packages and devDependencies (useful for production builds):

`npm prune --production`

- Show what would be removed without making any changes:

`npm prune --dry-run`

- Output the changes as JSON:

`npm prune --json`

- Remove specific packages by name:

`npm prune {{package_name}}`

- Prune packages in all configured workspaces:

`npm prune --workspaces`
