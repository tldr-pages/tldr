# jj

> Jujutsu, a version control system.
> Some subcommands such as `log`, `desc`, `new`, `git fetch`, etc. have their own usage documentation.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/>.

- Update description of the given revision(s):

`jj describe {{[-r|--revision]}} {{revsets}}`

- Create a new commit/revision on top of the given revision(s):

`jj new {{revsets}}`

- Execute a jj subcommand without snapshotting the working copy:

`jj --ignore-working-copy {{subcommand}}`

- Execute a jj subcommand at an operation:

`jj {{[--at-op|--at-operation]}} {{operation}} {{subcommand}}`

- Display help for a specific subcommand (like `new`, `commit`, `desc`, etc.):

`jj help {{subcommand}}`
