# npm link

> Symlink a local package into the global `node_modules` or another project for development.
> More information: <https://docs.npmjs.com/cli/npm-link>.

- Symlink the current package globally:

`npm link`

- Link a globally linked package into another project's `node_modules`:

`npm link {{package_name}}`

- Unlink a package from the current project:

`npm unlink {{package_name}}`
