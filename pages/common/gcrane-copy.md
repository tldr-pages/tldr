# gcrane copy

> Efficiently copy a remote image from source to target while retaining the digest value.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Copy an image from source to target:

`gcrane copy/cp {{source}} {{target}}`

- Display help:

`gcrane copy {{-h|--help}}`

- Set the maximum number of concurrent copies, defaults to GOMAXPROCS:

`gcrane copy {{source}} {{target}} {{-j|--jobs}} {{int}}`

- Whether to recurse through repositories:

`grance copy {{source}} {{target}} {{-r|--recursive}}`
