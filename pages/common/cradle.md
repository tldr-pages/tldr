# cradle

> The Cradle PHP framework.
> Some subcommands such as `install` and `package` have their own usage documentation.
> More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html>.

- Install Cradle components (prompts for additional info):

`cradle install`

- Force install and overwrite files:

`cradle install {{[-f|--force]}}`

- Connect to a remote server (see `config/deploy.php`):

`cradle connect {{server_name}}`

- Display the current Cradle configuration:

`cradle config show`

- Install a package into the current Cradle instance:

`cradle package install {{package_name}}`

- List installed packages:

`cradle package list`

- Display help:

`cradle help`

- Display version:

`cradle --version`
