# gofmt

> Gofmt formats Go programs. It uses tabs for indentation and blanks for alignment.

- Format a file and print it to output:

`gofmt {{source.go}}`

- Format a file and rewrite original:

`gofmt {{source.go}} -w`

- Print all (including spurious) errors:

`gofmt {{source.go}} -e`

- Apply custom rule as string "pattern -> replacement":

`gofmt {{source.go}} -r {{rule}}`
