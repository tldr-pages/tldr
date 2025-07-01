# jj

> Jujutsu, a version control system.
> Some subcommands such as `log`, `desc`, `new`, `git`, etc. have their own usage documentation.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/>.

- Update description of the revisions specified by given revsets (e.g. `B::D`, `A..D`, `B|C|D`, etc.):

`jj describe {{[-r|--revision]}} {{revsets}}`

- Create a new commit/revision on top of the revisions specified by the given revsets:

`jj new {{revsets}}`

- Execute a jj subcommand without snapshotting the working copy:

`jj --ignore-working-copy {{subcommand}}`

- Execute a jj subcommand at an operation:

`jj {{[--at-op|--at-operation]}} {{operation}} {{subcommand}}`

- Display help for a specific subcommand (like `new`, `commit`, `desc`, etc.):

`jj help {{subcommand}}`
