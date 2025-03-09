# npm install

> Install Node packages.
> More information: <https://docs.npmjs.com/cli/commands/npm-install>.

- Install dependencies listed in `package.json`:

`npm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`npm install {{package_name}}@{{version}}`

- Download the latest version of a package and add it to the list of dev dependencies in `package.json`:

`npm install {{package_name}} {{[-D|--save-dev]}}`

- Download the latest version of a package and install it globally:

`npm install {{[-g|--global]}} {{package_name}}`
