# shfmt

> Shell parser, formatter, and interpreter.
> More information: <https://pkg.go.dev/mvdan.cc/sh#section-readme>.

- Print a formatted version of a shell script:

`shfmt {{path/to/file}}`

- List unformatted files:

`shfmt {{[-l|--list]}} {{path/to/directory}}`

- Write the result to the file instead of printing it to the terminal:

`shfmt {{[-w|--write]}} {{path/to/file}}`

- Simplify the code, removing redundant pieces of syntax (e.g. removing "$" from vars in expressions):

`shfmt {{[-s|--simplify]}} {{path/to/file}}`

- Specify the amount of spaces to use for indentation (0 for tabs, which is also the default):

`shfmt {{[-i|--indent]}} {{4}} {{path/to/file}}`

- Format the code according to Google's style guide:

`shfmt {{[-i|--indent]}} 2 {{[-ci|--case-indent]}} {{[-w|--write]}} {{path/to/file}}`
