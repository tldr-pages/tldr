# git for-each-repo

> Run a Git command on a list of repositories.
> This command is experimental. **The behavior may change**.
> More information: <https://git-scm.com/docs/git-for-each-repo>.

- Run maintenance on each of a list of repositories stored in a `maintenance.repo` configuration variable:

`git for-each-repo --config={{maintenance.repo}} {{maintenance run}}`

- Run `git pull` on each repository from a specific configuration variable:

`git for-each-repo --config={{configuration_variable}} {{pull}}`
