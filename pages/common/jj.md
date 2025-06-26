# jj

> Jujutsu - Version control system.
> Some subcommands such as `log`, `new`, `git fetch`, `git push`, etc. have their own usage documentation.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/>.

- Execute a jj subcommand:

`jj {{subcommand}`

- Execute a jj subcommand without snapshotting the working copy:

`jj --ignore-working-copy {{subcommand}}`

- Execute a jj subcommand at an operation:

`jj {{[--at-op|--at-operation]}} {{operation}} {{subcommand}}`

- Display help for a specific subcommand (like `new`, `commit`, `desc`, etc.):

`jj help {{subcommand}}`
