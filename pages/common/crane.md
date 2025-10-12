# crane

> Container images managing tool.
> Some subcommands such as `pull`, `push`, `copy`, etc. have their own usage documentation.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Log in to a registry:

`crane auth login {{registry}} {{[-u|--username]}} {{user}} {{[-p|--password]}} {{password}}`

- List the repos in a registry:

`crane catalog {{registry}} --full-ref`

- List the tags in a repository:

`crane ls {{repository}} {{[-o|--omit-digest-tags]}}`

- Pull remote images by reference and store their contents locally:

`crane pull {{image}} {{tarball}}`

- Push local image contents to a remote registry:

`crane push {{path/to/directory_or_tarball}} {{image}}`

- Efficiently tag a remote image:

`crane tag {{image}} {{tag}}`

- Efficiently copy a remote image from `src` to `dst` while retaining the digest value:

`crane copy src dst {{[-a|--all-tags]}}`

- Delete an image reference from its registry:

`crane delete {{image}}`
