# bun pm pkg

> Manage package.json data with `get`, `set`, `delete`, and `fix` operations.
> More information: <https://bun.com/docs/pm/cli/pm#pkg>.

- Get all properties from `package.json`:

`bun pm pkg get`

- Get a single property:

`bun pm pkg get {{property}}`

- Get multiple properties:

`bun pm pkg get {{property1 property2 property3 ...}}`

- Set a property:

`bun pm pkg set {{property}}="{{value}}"`

- Delete a property:

`bun pm pkg delete {{property}}`

- Automatically fix common issues in `package.json`:

`bun pm pkg fix`
