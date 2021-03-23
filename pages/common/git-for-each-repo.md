# git for-each-repo

> Run a Git command on a list of repositories.
> Note: this command is experimental and may change.
> More information: <https://git-scm.com/docs/git-for-each-repo>.

- Run maintenance on each of a list of repositories stored in the `maintenance.repo` user configuration variable:

`git for-each-repo --config={{maintenance.repo}} {{maintenance run}}`

- Run `git pull` on each repository listed in a global configuration variable:

`git for-each-repo --config={{global_configuration_variable}} {{pull}}`
