# git tag

> Create, list, delete or verify tags.
> A tag is a static reference to a commit.
> More information: <https://git-scm.com/docs/git-tag>.

- List all tags:

`git tag`

- Create a tag with the given name pointing to the current commit:

`git tag {{tag_name}}`

- Create a tag with the given name pointing to a given commit:

`git tag {{tag_name}} {{commit}}`

- Create an annotated tag with the given message:

`git tag {{tag_name}} -m {{tag_message}}`

- Delete the tag with the given name:

`git tag -d {{tag_name}}`

- Get updated tags from upstream:

`git fetch --tags`

- List all tags whose ancestors include a given commit:

`git tag --contains {{commit}}`
