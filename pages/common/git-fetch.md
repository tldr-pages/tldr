# git fetch

> Download objects and refs from a remote repository.
> More information: <https://git-scm.com/docs/git-fetch>.

- Fetch the latest changes from the default remote upstream repository (if set):

`git fetch`

- Fetch new branches from a specific remote upstream repository:

`git fetch {{remote_name}}`

- Fetch the latest changes from all remote upstream repositories:

`git fetch --all`

- Also fetch tags from the remote upstream repository:

`git fetch {{[-t|--tags]}}`

- Delete local references to remote branches that have been deleted upstream:

`git fetch {{[-p|--prune]}}`

- Deepen current shallow branch by 2 commits:

`git fetch --deepen 2`

- Update the `main` branch without switching to it (equivalent to `git pull`):

`git fetch {{origin}} main:main`
