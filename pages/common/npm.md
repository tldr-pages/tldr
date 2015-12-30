# npm

> Node package manager, to manage Node.js projects and install module dependencies.

- Create a new project in the current folder

`npm init`

- Download all dependencies referenced in package.json

`npm install`

- Download a given dependency, and add it to the package.json

`npm install {{module_name}}@{{version}} --save`

- Set the version of the current project

`npm version {{1.2.3}}`

- Publish the current project

`npm publish`

- Cleanup packages (removes packages, which are installed but are not listed in `package.json`)

`npm prune`
