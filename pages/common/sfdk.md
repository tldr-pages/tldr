# sfdk

> The command line frontend of the Sailfish SDK.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/10-general/doc/module.adoc>.

- Execute a subcommand:

`sfdk {{subcommand}}`

- Execute a subcommand on a custom working directory:

`git -C {{path/to/directory}} {{subcommand}}`

- Execute a subcommand with a given configuration set:

`git -c '{{name}}={{value}}' {{subcommand}}`

- Display help:

`sfdk {{[-h|--help]}}`

- Display help for specific topic (`building`, `testing`, `maintaining`, `ide`, `all`):

`sfdk --help-{{topic}}`

- Display version:

`sfdk --version`
