# yarn

> JavaScript and Node.js package manager alternative.

- Install a module globally:

`yarn global add {{module_name}}`

- Install all dependencies referenced in the package.json:

`yarn`

- Install a module and save it as a dependency to the package.json:

`yarn add {{module_name}}@{{version}}`

- Install a module and save it as a dev dependency to the package.json:

`yarn add {{module_name}}@{{version}} --dev`

- Uninstall a module and remove it from the package.json:

`yarn remove {{module_name}}`

- List a tree of installed modules:

`yarn ls`

- Interactively create a package.json file:

`yarn init`

- Identify why the module is installed and list other modules that depend on it:

`yarn why {{module_name}}`
