# sfdk

> The command line frontend of the Sailfish SDK.
> More information: <https://docs.sailfishos.org/Develop/Apps/Tutorials/Building_packages_-_advanced_techniques/>.

- Execute a subcommand:

`sfdk {{subcommand}}`

- Execute a subcommand on a custom working directory:

`git -C {{path/to/directory}} {{subcommand}}`

- Execute a subcommand with a given configuration set:

`git -c '{{name}}={{value}}' {{subcommand}}`

- Display help:

`sfdk --help`

- Display help for specific topic (`building`, `testing`, `maintaining`, `ide`, `all`):

`sfdk --help-{{topic}}`

- Display version:

`sfdk --version`
