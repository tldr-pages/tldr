# pnpm

> Fast, disk space efficient package manager for Node.js.
> Manage Node.js projects and their module dependencies.
> More information: <https://pnpm.io/pnpm-cli>.

- Create a `package.json` file:

`pnpm init`

- Download all the packages listed as dependencies in `package.json`:

`pnpm {{[i|install]}}`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`pnpm add {{module_name}}@{{version}}`

- Download a package and add it to the list of dev dependencies in `package.json`:

`pnpm add {{[-D|--save-dev]}} {{module_name}}`

- Download a package and install it globally:

`pnpm add {{[-g|--global]}} {{module_name}}`

- Uninstall a package and remove it from the list of dependencies in `package.json`:

`pnpm {{[rm|remove]}} {{module_name}}`

- Print a tree of locally installed modules:

`pnpm {{[ls|list]}}`

- List top-level globally installed modules:

`pnpm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
