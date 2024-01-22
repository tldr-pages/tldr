# git

> Distributed version control system.
> Some subcommands such as `commit`, `add`, `branch`, `checkout`, `push`, etc. have their own usage documentation.
> More information: <https://git-scm.com/>.

- Execute a Git subcommand:

`git {{subcommand}}`

- Execute a Git subcommand on a custom repository root path:

`git -C {{path/to/repo}} {{subcommand}}`

- Execute a Git subcommand with a given configuration set:

`git -c '{{config.key}}={{value}}' {{subcommand}}`

- Display help:

`git --help`

- Display help for a specific subcommand (like `clone`, `add`, `push`, `log`, etc.):

`git help {{subcommand}}`

- Display version:

`git --version`
