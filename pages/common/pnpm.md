# pnpm

> Fast, disk space efficient package manager for Node.js.
> Manage Node.js projects and their module dependencies.
> More information: <https://pnpm.io>.

- Create a `package.json` file:

`pnpm init`

- Download all the packages listed as dependencies in `package.json`:

`pnpm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`pnpm add {{module_name}}@{{version}}`

- Download a package and add it to the list of [D]ev dependencies in `package.json`:

`pnpm add -D {{module_name}}`

- Download a package and install it [g]lobally:

`pnpm add -g {{module_name}}`

- Uninstall a package and remove it from the list of dependencies in `package.json`:

`pnpm remove {{module_name}}`

- Print a tree of locally installed modules:

`pnpm list`

- List top-level [g]lobally installed modules:

`pnpm list -g --depth={{0}}`
