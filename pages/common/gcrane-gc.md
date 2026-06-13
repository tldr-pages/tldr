# gcrane gc

> List images that are not tagged.
> Will calculate images that can be garbage-collected.
> This can be composed with `gcrane delete` to actually garbage collect them.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- List untagged images:

`gcrane gc {{repository}}`

- Whether to recurse through repositories:

`gcrane gc {{repository}} {{[-r|--recursive]}}`

- Display help:

`gcrane gc {{[-h|--help]}}`
