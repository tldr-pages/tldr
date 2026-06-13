# gcrane copy

> Efficiently copy a remote image from source to target while retaining the digest value.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Copy an image from source to target:

`gcrane {{[cp|copy]}} {{source}} {{target}}`

- Set the maximum number of concurrent copies, defaults to 20:

`gcrane copy {{source}} {{target}} {{[-j|--jobs]}} {{nr_of_copies}}`

- Whether to recurse through repositories:

`gcrane copy {{source}} {{target}} {{[-r|--recursive]}}`

- Display help:

`gcrane copy {{[-h|--help]}}`
