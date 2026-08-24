# jj tag

> Manage tags in a `jj` repository.
> Some subcommands such as `delete`, `list`, `set` have their own usage documentation.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag>.

- Create a tag pointing to the current working copy revision:

`jj tag {{[s|set]}} {{tag_name}}`

- Create a tag pointing to a specific revision:

`jj tag {{[s|set]}} {{tag_name}} {{[-r|--revision]}} {{revision}}`

- List all tags:

`jj tag {{[l|list]}}`

- List tags matching a pattern, sorted by committer date (newest first):

`jj tag {{[l|list]}} --sort committer-date- "{{pattern}}"`

- Move an existing tag to a different revision:

`jj tag {{[s|set]}} {{tag_name}} {{[-r|--revision]}} {{revision}} --allow-move`

- Delete a tag:

`jj tag {{[d|delete]}} {{tag_name}}`

- Delete tags matching a glob pattern:

`jj tag {{[d|delete]}} "{{glob:v1.*}}"`

- Display help:

`jj tag {{[-h|--help]}}`
