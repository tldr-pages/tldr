# bun remove

> Remove a dependency from `package.json`.
> More information: <https://bun.sh/docs/cli/remove>.

- Remove a dependency:

`bun {{[rm|remove]}} {{package_name}}`

- Remove multiple dependencies:

`bun {{[rm|remove]}} {{package_name1 package_name2 ...}}`

- Remove a globally installed package:

`bun {{[rm|remove]}} {{[-g|--global]}} {{package_name}}`

- Remove a dependency without updating the `package.json` file:

`bun {{[rm|remove]}} --no-save {{package_name}}`

- Run the command without actually removing packages (simulate the removal):

`bun {{[rm|remove]}} --dry-run {{package_name}}`
