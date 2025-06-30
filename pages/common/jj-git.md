# jj git

> Run Git-related commands for a `jj` repository.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git>.

- Create a new Git backed repository:

`jj git init`

- Create a new repository backed by a clone of a Git repository:

`jj git clone {{source}}`

- Fetch from a Git remote:

`jj git fetch`

- Push all tracked bookmarks to Git remote:

`jj git push`

- Push given bookmark to Git remote:

`jj git push {{[-b|--bookmark]}} {{bookmark}}`
