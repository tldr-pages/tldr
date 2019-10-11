# goreload

> Live reload utility for Go programs.
> More information: <https://github.com/acoshift/goreload>.

- Set the name of the binary file to watch (defaults to ".goreload"):

`goreload -b {{path/to/binary}} {{file}}.go`

- Set a custom log prefix (defaults to "goreload"):

`goreload --logPrefix {{prefix}} {{file}}.go`

- Reload whenever any file changes:

`goreload --all`
