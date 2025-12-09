# goreload

> Live reload utility for Go programs.
> More information: <https://github.com/acoshift/goreload#basic-usage>.

- Watch a binary file (defaults to `.goreload`):

`goreload {{[-b|--bin]}} {{path/to/binary}} {{path/to/file.go}}`

- Set a custom log prefix (defaults to `goreload`):

`goreload --logPrefix {{prefix}} {{path/to/file.go}}`

- Reload whenever any file changes:

`goreload --all`
