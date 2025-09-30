# jj bookmark

> Manage bookmarks in a `jj` repository.
> When using a Git backend, bookmarks correspond to Git branches.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-bookmark>.

- Create a new bookmark at the given revision:

`jj {{[b|bookmark]}} {{[c|create]}} {{[-r|--revision]}} {{revision}} {{name}}`

- List all existing bookmarks and their targets:

`jj {{[b|bookmark]}} {{[l|list]}}`

- Move an existing bookmark to another revision:

`jj {{[b|bookmark]}} {{[m|move]}} {{[-t|--to]}} {{revision}} {{name}}`

- Track given remote bookmarks:

`jj {{[b|bookmark]}} {{[t|track]}} {{name}}@{{remote}}`

- Delete a bookmark, and propagate the deletion to remotes on the next push:

`jj {{[b|bookmark]}} {{[d|delete]}} {{name}}`

- Forget a bookmark locally, without marking its deletion to be pushed:

`jj {{[b|bookmark]}} {{[f|forget]}} {{name}}`
