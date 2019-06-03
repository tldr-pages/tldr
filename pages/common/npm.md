# npm

> JavaScript and Node.js package manager.
> Manage Node.js projects and their module dependencies.
> More information: <https://www.npmjs.com/>.

- Interactively create a package.json file:

`npm init`

- Download all the packages listed as dependencies in package.json:

`npm install`

- Download a specific version of a package and add it to the list of dependencies in package.json:

`npm install {{module_name}}@{{version}}`

- Download a package and add it to the list of dev dependencies in package.json:

`npm install {{module_name}} --save-dev`

- Download a package and install it globally:

`npm install -g {{module_name}}`

- Uninstall a package and remove it from the list of dependencies in package.json:

`npm uninstall {{module_name}}`

- Print a tree of locally-installed dependencies:

`npm list`

- List top-level globally installed modules:

`npm list -g --depth={{0}}`
