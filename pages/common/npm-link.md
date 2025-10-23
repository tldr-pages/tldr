# npm-link

> Symlink a local package into the global `node_modules` or another project for development.
> Useful for working on dependencies locally.
> More information: <https://docs.npmjs.com/cli/v10/commands/npm-link>.

- Symlink the current package globally:

`npm link`

- Link a globally linked package into another project's `node_modules`:

`npm link {{package_name}}`

- Unlink a package from the current project:

`npm unlink {{package_name}}`
