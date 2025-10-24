# npm pkg

> Show or modify `package.json` properties.
> More information: <https://docs.npmjs.com/cli/v9/commands/npm-pkg>.

- Get the value of a specific property:

`npm {{pkg}} get {{name}}`

- Get multiple properties at once:

`npm {{pkg}} get {{name}} {{version}}`

- Get a nested or array property value:

`npm {{pkg}} get {{contributors[0].email}}`

- Set a property to a specific value:

`npm {{pkg}} set {{version=1.2.3}}`

- Set multiple properties at once:

`npm {{pkg}} set {{description='Awesome package'}} {{engines.node='>=10'}}`

- Delete a property from `package.json`:

`npm {{pkg}} delete {{scripts.build}}`

- Auto-fix common errors in `package.json`:

`npm {{pkg}} fix`

- Get or set values across all workspaces:

`npm {{pkg}} get {{name}} {{version}} --ws`
