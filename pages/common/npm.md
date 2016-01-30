# npm

> JavaScript and Node.js package manager.
> Manage Node.js projects and their module dependencies.

- Download and install a module globally:

`npm install -g {{module_name}}`

- Download all dependencies referenced in package.json:

`npm install`

- Download a given dependency, and add it to the package.json:

`npm install {{module_name}}@{{version}} --save`

- Uninstall a module:

`npm uninstall {{module_name}}`

- List a tree of installed modules:

`npm list`

- Interactively create a package.json file:

`npm init`
