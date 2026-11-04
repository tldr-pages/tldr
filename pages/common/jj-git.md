# jj git

> Run Git-related commands for a `jj` repository.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git>.

- Create a new Git backed repository:

`jj git init`

- Create a new repository backed by a clone of a Git repository:

`jj git clone {{source}}`

- Clone a Git repository as a `jj` repository, without colocation:

`jj git clone --no-colocate {{source}}`

- Fetch from a Git remote:

`jj git fetch`

- Push all tracked bookmarks to Git remote:

`jj git push`

- Push given bookmark to Git remote:

`jj git push {{[-b|--bookmark]}} {{bookmark}}`

- Convert into a colocated Jujutsu/Git repository:

`jj git colocation enable`

- Show the path to the underlying Git directory:

`jj git root`
