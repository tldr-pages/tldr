# crane copy

> Efficiently copy a remote image from source to target while retaining the digest value.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- Copy an image from source to target:

`crane {{[cp|copy]}} {{source}} {{target}}`

- Copy all tags:

`crane {{[cp|copy]}} {{source}} {{target}} {{[-a|--all-tags]}}`

- Set the maximum number of concurrent copies, defaults to GOMAXPROCS:

`crane {{[cp|copy]}} {{source}} {{target}} {{[-j|--jobs]}} {{int}}`

- Avoid overwriting existing tags in target:

`crane {{[cp|copy]}} {{source}} {{target}} {{[-n|--no-clobber]}}`

- Display help:

`crane {{[cp|copy]}} {{[-h|--help]}}`
