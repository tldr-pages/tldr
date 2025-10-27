# npm pkg

> Show or modify `package.json` properties.
> More information: <https://docs.npmjs.com/cli/commands/npm-pkg>.

- Get the value of a specific property:

`npm pkg get {{name}}`

- Get multiple properties at once:

`npm pkg get {{name}} {{version}}`

- Get a nested or array property value:

`npm pkg get {{contributors[0].email}}`

- Set a property to a specific value:

`npm pkg set {{property}}={{value}}`

- Set multiple properties at once:

`npm pkg set {{property1}}={{value1}} {{property2}}={{value2}}`

- Delete a property from `package.json`:

`npm pkg delete {{scripts.build}}`

- Auto-fix common errors in `package.json`:

`npm pkg fix`

- Get multiple values across all workspaces:

`npm pkg get {{name}} {{version}} --ws`
