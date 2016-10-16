# yarn

> JavaScript and Node.js package manager alternative.

- Install a module globally:

`yarn global add {{module_name}}`

- Install all dependencies referenced in the package.json:

`yarn`

- Install a module and save it as a dependency to the package.json. Add --dev to save as a dev dependency:

`yarn add {{module_name}}@{{version}}`

- Uninstall a module and remove it from the package.json:

`yarn remove {{module_name}}`

- Interactively create a package.json file:

`yarn init`

- Identify why the module is installed and list other modules that depend on it:

`yarn why {{module_name}}`
