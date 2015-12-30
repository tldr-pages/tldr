# npm

> Node package manager, to manage Node.js projects and install module dependencies.

- Create a new project in the current folder

`npm init`

- Download all dependencies referenced in package.json

`npm install`

- Download and install a module globally

`npm install -g {{module_name}}`

- Download a given dependency, and add it to the package.json

`npm install {{module_name}}@{{version}} --save`

- Set the version of the current project

`npm version {{1.2.3}}`

- Publish the current project

`npm publish`
