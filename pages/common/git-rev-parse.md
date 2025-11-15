# git rev-parse

> Display metadata related to revisions.
> More information: <https://git-scm.com/docs/git-rev-parse>.

- Get the commit hash of a branch:

`git rev-parse {{branch_name}}`

- Get the current branch name:

`git rev-parse --abbrev-ref {{HEAD}}`

- Get the absolute path to the root directory:

`git rev-parse --show-toplevel`
