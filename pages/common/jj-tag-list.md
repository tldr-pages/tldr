# jj tag list

> List tags in a `jj` repository.
> See also: `jj tag delete`, `jj tag set`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag-list>.

- List all tags:

`jj tag {{[l|list]}}`

- List tags matching a pattern:

`jj tag {{[l|list]}} "{{pattern}}"`

- List tags matching a substring pattern:

`jj tag {{[l|list]}} "{{substring:release}}"`

- List tags sorted by committer date (newest first):

`jj tag {{[l|list]}} --sort committer-date-`

- List tags sorted by name in descending order:

`jj tag {{[l|list]}} --sort name-`

- List tags with a custom template:

`jj tag {{[l|list]}} {{[-T|--template]}} "{{template}}"`
