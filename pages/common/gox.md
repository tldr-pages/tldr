# gox

> A tool for Go cross compilation.

- Compile current Go directory for all OS and arch:

`gox`

- Compile from URL:

`gox {{url_1}} {{url_2}}`

- Compile current directory for `{{os}}`:

`gox -os="{{os}}"`

- Compile current directory for `{{os}}` running `{{arch}}`:

`gox -osarch="{{os}}/{{arch}}"`
