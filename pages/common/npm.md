# npm

> JavaScript and Node.js package manager.
> Manage Node.js projects and their module dependencies.
> More information: <https://www.npmjs.com>.

- Create a `package.json` file with default values (omit `--yes` to do it interactively):

`npm init {{-y|--yes}}`

- Download all the packages listed as dependencies in `package.json`:

`npm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`npm install {{package_name}}@{{version}}`

- Download the latest version of a package and add it to the list of dev dependencies in `package.json`:

`npm install {{package_name}} {{-D|--save-dev}}`

- Download the latest version of a package and install it globally:

`npm install {{-g|--global}} {{package_name}}`

- Uninstall a package and remove it from the list of dependencies in `package.json`:

`npm uninstall {{package_name}}`

- List all locally installed dependencies:

`npm list`

- List all top-level globally installed packages:

`npm list {{-g|--global}} --depth {{0}}`
