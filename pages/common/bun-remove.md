# bun remove

> Remove a dependency from `package.json`.
> Note: `rm` can be used as an alias for `remove`.
> More information: <https://bun.sh/docs/cli/remove>.

- Remove a dependency:

`bun remove {{package_name}}`

- Remove multiple dependencies:

`bun remove {{package_name1 package_name2 ...}}`

- Remove a globally installed package:

`bun remove {{[-g|--global]}} {{package_name}}`

- Remove a dependency without updating the `package.json` file:

`bun remove --no-save {{package_name}}`

- Run the command without actually removing packages (simulate the removal):

`bun remove --dry-run {{package_name}}`
