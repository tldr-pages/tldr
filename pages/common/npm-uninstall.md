# npm uninstall

> Remove a package.
> More information: <https://docs.npmjs.com/cli/v8/commands/npm-uninstall>.
- Remove a package from the project:

`npm uninstall {{package_name}}`

- Remove a package globally:

`npm uninstall -g {{package_name}}`

- Remove multiple packages at once:

`npm uninstall {{package_name1}} {{package_name2}}`

- Remove a package and all its dependencies that are no longer needed:

`npm uninstall {{package_name}} --save`

- Remove a package and update `package.json`:

`npm uninstall {{package_name}} --save-dev`
