# crane tag

> Efficiently tag a remote image without downloading it.
> This differs slightly from the "copy" command in a couple subtle ways.
> You don't have to specify the entire repository for the tag you're adding.
> We can skip layer existence checks because we know the manifest already exists. This makes "tag" slightly faster than "copy".
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

- Tag remote image:

`crane tag {{image_name}} {{tag_name}}`

- Display help:

`crane tag {{-h|--help}}`
