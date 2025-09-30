# crane copy

> Efficiently copy a remote image from source to target while retaining the digest value.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- Copy an image from source to target:

`crane copy {{source}} {{target}}`

- Copy all tags:

`crane copy {{source}} {{target}} {{[-a|--all-tags]}}`

- Set the maximum number of concurrent copies, defaults to GOMAXPROCS:

`crane copy {{source}} {{target}} {{[-j|--jobs]}} {{int}}`

- Avoid overwriting existing tags in target:

`crane copy {{source}} {{target}} {{[-n|--no-clobber]}}`

- Display help:

`crane copy {{[-h|--help]}}`
