# gcrane ls

> List the tags in a repository.
> More complex form than `crane ls`, which allows for listing tags, manifest and sub-repositories.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- List the tags:

`gcrane ls {{repository}}`

- Format response from the registry as JSON:

`gcrane ls {{repository}} --json`

- Whether to recurse through repositories:

`gcrane ls {{repository}} {{[-r|--recursive]}}`

- Display help:

`gcrane ls {{[-h|--help]}}`
