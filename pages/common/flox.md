# flox

> Easy to use Nix package and environment manager.
> More information: <https://flox.dev/docs/reference/command-reference/flox/>.

- Create a new environment in the current directory:

`flox init`

- Enter an environment, or create one if it doesn't exist:

`flox activate`

- Search for packages in the FloxHub catalog:

`flox search {{package}}`

- Install a package into the current environment:

`flox {{[i|install]}} {{package}}`

- Uninstall a package from the current environment:

`flox uninstall {{package}}`

- View a list of all packages installed in the current environment:

`flox {{[l|list]}}`

- Push a local environment to FloxHub to share with others:

`flox push`

- Pull a shared environment from FloxHub:

`flox pull {{environment_name}}`
