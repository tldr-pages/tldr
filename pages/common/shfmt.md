# shfmt

> A shell parser, formatter and interpreter.
> More information: <https://pkg.go.dev/mvdan.cc/sh/v3>.

- Print a formatted version of a shell script:

`shfmt {{path/to/file}}`

- List unformatted files:

`shfmt --list {{path/to/directory}}`

- Write result to file instead of printing to terminal:

`shfmt --write {{path/to/file}}`

- Simplify the code:

`shfmt --simplify {{path/to/file}}`
