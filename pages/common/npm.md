# npm

> JavaScript and Node.js package manager.  Manage Node.js projects and their module dependencies.

- Suppress standard npm progress bar:

`npm set progress=false`

- Find out which npm packages are outdated:

`npm outdated`

- Update npm packages:

`npm update {{module_name}}`

- List all packages install by user:

`npm list -depth=0`

- If you'd like to see all available (remote) versions for a particular package:
  
`npm view <module_name> versions`

- Search for npm packages:

`npm search {{module_name}}`

- View details of a npm package:

`npm view {{module_name}}`

- Download and install a module globally:

`npm install -g {{module_name}}`

- Download all dependencies referenced in package.json:

`npm install`

- Download a given dependency required for the application to run, and add it to the package.json:

`npm install {{module_name}}@{{version}} --save`

- Download a given dependency for development purposes, and add it to the package.json:

`npm install {{module_name}}@{{version}} --save-dev`

- Uninstall a module:

`npm uninstall {{module_name}}`

- List a tree of installed modules:

`npm list`

- Interactively create a package.json file:

`npm init`
