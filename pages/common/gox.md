# gox

> A tool for cross-compiling Go programs.

- Compile Go program in the current directory for all operating systems and architecture combinations:

`gox`

- Download and compile a Go program from a remote URL:

`gox {{url_1}} {{url_2}}`

- Compile current directory for `{{os}}`:

`gox -os="{{os}}"`

- Compile current directory for `{{os}}` running `{{arch}}`:

`gox -osarch="{{os}}/{{arch}}"`
