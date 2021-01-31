# bower

> A package manager optimized for front-end web development.
> A package can be a GitHub user/repo shorthand, a Git endpoint, a URL or a registered package.
> More information: <https://bower.io/>.

- Install a project's dependencies, listed in its bower.json:

`bower install`

- Install one or more packages to the bower_components directory:

`bower install {{package}} {{package}}`

- Uninstall packages locally from the bower_components directory:

`bower uninstall {{package}} {{package}}`

- List local packages and possible updates:

`bower list`

- Display help information about a bower command:

`bower help {{command}}`

- Create a `bower.json` file for your package:

`bower init`

- Install a specific dependency version, and add it to `bower.json`:

`bower install {{local_name}}={{package}}#{{version}} --save`
