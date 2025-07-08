# jj git clone

> Create a new repo backed by a clone of a Git repo.
> Note: Unless `--colocate` is used, it is not a valid Git repository and `git` commands can't be used on it.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-clone>.

- Create a new repo backed by a clone of a Git repo into a new directory (the default directory is the repository name):

`jj git clone {{source}} {{path/to/directory}}`

- Create a clone and use the given name for newly created remote:

`jj git clone --remote {{remote_name}} {{source}}`

- Clone a Git repo, only fetching the 10 most recent commits:

`jj git clone --depth {{10}} {{source}}`

- Clone colocating the Jujutsu repo with the Git repo (allowing the use of both `jj` and `git` commands in the same directory):

`jj git clone --colocate {{source}}`
