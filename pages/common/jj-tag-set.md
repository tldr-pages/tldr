# jj tag set

> Create or update tags in a `jj` repository.
> See also: `jj tag delete`, `jj tag list`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag-set>.

- Create a tag pointing to the current working copy revision:

`jj tag {{[s|set]}} {{tag_name}}`

- Create a tag pointing to a specific revision:

`jj tag {{[s|set]}} {{tag_name}} {{[-r|--revision]}} {{revision}}`

- Create multiple tags pointing to the same revision:

`jj tag {{[s|set]}} {{tag1 tag2 ...}} {{[-r|--revision]}} {{revision}}`

- Move an existing tag to a different revision:

`jj tag {{[s|set]}} {{tag_name}} {{[-r|--revision]}} {{revision}} --allow-move`

- Create a tag pointing to a parent of the current revision:

`jj tag {{[s|set]}} {{tag_name}} {{[-r|--revision]}} @-`
