# dvc

> Data Version Control is a command-line tool designed to bring version control capabilities to data.
> Some subcommands such as `commit` have their own usage documentation.
> More information: <https://dvc.org/doc/command-reference>.

- Initialize a new DVC project:

`dvc init`

- Add one or more data files or directories to tracking:

`dvc add {{path/to/file_or_directory}}`

- Execute a specific subcommand:

`dvc {{subcommand}}`

- Display help:

`dvc {{[-h|--help]}}`

- Display help about a specific subcommand:

`dvc {{subcommand}} {{[-h|--help]}}`

- Display version:

`dvc --version`
