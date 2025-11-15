# jj git fetch

> Fetch from a Git remote, downloading objects and refs from the remote repository.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-fetch>.

- Fetch the latest changes from the default remote repository:

`jj git fetch`

- Fetch the latest changes from a given remote repository:

`jj git fetch --remote {{remote}}`

- Fetch the latest changes only from given branches:

`jj git fetch {{[-b|--branch]}} {{branch}}`

- Fetch the latest changes from all remotes:

`jj git fetch --all-remote`
