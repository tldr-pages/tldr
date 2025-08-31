# flox

> A next-generation package and virtual environment manager.
> Flox allows you to create reproducible development environments that are portable across multiple platforms and can be shared with others.
> More information: <https://flox.dev/docs/>.

- Create a new environment in the current directory:

`flox init`

- Enter an environment, or create one if it doesn't exist:

`flox activate`

- Search for packages in the FloxHub catalog:

`flox search {{package}}`

- Install a package into the current environment:

`flox install {{package}}`

- Uninstall a package from the current environment:

`flox uninstall {{package}}`

- View a list of all packages installed in the current environment:

`flox list`

- Push a local environment to FloxHub to share with others:

`flox push`

- Pull a shared environment from FloxHub:

`flox pull {{environment_name}}`
