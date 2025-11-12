# cradle

> The Cradle PHP framework command-line tool.
> Some subcommands such as `install` and `package` have their own usage documentation.
> More information: <https://cradlephp.github.io>.

- Install Cradle components (prompts for additional info):

`cradle install`

- Force install and overwrite files:

`cradle install --force`

- Connect to a remote server (see `config/deploy.php`):

`cradle connect {{server_name}}`

- Execute a Cradle command or subcommand:

`cradle {{command}}`

- Install a package into the current Cradle instance:

`cradle package install {{package_name}}`

- List installed packages:

`cradle package list`

- Display general help:

`cradle help`

- Show version information:

`cradle --version`
