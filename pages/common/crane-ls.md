# crane ls

> List the tags in a repository.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_ls.md>.

- List the tags:

`crane ls {{repository}}`

- Print the full image reference:

`crane ls {{repository}} --full-ref`

- Omit digest tags:

`crane ls {{[-o|--omit-digest-tags]}}`

- Display help:

`crane ls {{[-h|--help]}}`
