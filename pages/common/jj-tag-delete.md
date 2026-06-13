# jj tag delete

> Delete tags in a `jj` repository.
> See also: `jj tag list`, `jj tag set`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag-delete>.

- Delete a tag:

`jj tag {{[d|delete]}} {{tag_name}}`

- Delete multiple tags:

`jj tag {{[d|delete]}} {{tag1 tag2 ...}}`

- Delete tags matching a glob pattern:

`jj tag {{[d|delete]}} "{{glob:v1.*}}"`

- Delete tags matching a substring pattern:

`jj tag {{[d|delete]}} "{{substring:release}}"`

- Delete a tag by exact name:

`jj tag {{[d|delete]}} "{{exact:v1.0.0}}"`
