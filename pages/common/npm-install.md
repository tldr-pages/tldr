# npm install

>Install a package.
>More information: https://docs.npmjs.com/cli/v8/commands/npm-install.

- Install a package in the project:

`npm install {{package_name}}`

- Install a package globally:

`npm install -g {{package_name}}`

- Install a specific version of a package:

`npm install {{package_name}}@{{version}}`

- Install all dependencies listed in package.json:

`npm install`

- Install a package and update package.json:

`npm install {{package_name}} --save`

- Install a package as a development dependency and update package.json:

`npm install {{package_name}} --save-dev`
