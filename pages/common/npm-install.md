# npm install

> Install Node packages.
> More information: <https://docs.npmjs.com/cli/npm-install>.

- Install dependencies listed in `package.json`:

`npm {{[i|install]}}`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`npm {{[i|install]}} {{package_name}}@{{version}}`

- Download the latest version of a package and add it to the list of dev dependencies in `package.json`:

`npm {{[i|install]}} {{[-D|--save-dev]}} {{package_name}}`

- Download the latest version of a package and install it globally:

`npm {{[i|install]}} {{[-g|--global]}} {{package_name}}`
