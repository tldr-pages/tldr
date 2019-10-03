# goreload

> Live reload utility for Go program.
> More information: https://github.com/acoshift/goreload.

- Set name of binary file (default: ".goreload"):

`goreload -b {{name}} {{file}}.go`

- Set custom log prefix (defailt: "goreload"):

`goreload --logPrefix {{prefix}} {{file}}.go`

- Reload whenever any file changes:

`goreload --all`
