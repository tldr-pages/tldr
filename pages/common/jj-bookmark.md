# jj bookmark

> Manage bookmarks in a `jj` repository.
> When using a Git backend, bookmarks correspond to Git branches.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-bookmark>.

- Create a new bookmark at the given revision:

`jj bookmark create {{[-r|--revision]}} {{revset}} {{name}}`

- List all existing bookmarks and their targets:

`jj bookmark list`

- Move an existing bookmark to another revision:

`jj bookmark move {{[-t|--to]}} {{revset}} {{name}}`

- Track given remote bookmarks:

`jj bookmark track {{name}}@{{remote}}`

- Delete a bookmark, and propagate the deletion to remotes on the next push:

`jj bookmark delete {{name}}`

- Forget a bookmark locally, without marking its deletion to be pushed:

`jj bookmark forget {{name}}`
