# zek

> Generate a Go struct from XML.
> More information: <https://github.com/miku/zek>.

- Generate a Go struct from a given XML from stdin and display output on stdout:

`cat {{path/to/input.xml}} | zek`

- Generate a Go struct from a given XML from stdin and send output to a file:

`curl -s {{https://url/to/xml}} | zek -o {{path/to/output.go}}`

- Generate an example Go program from a given XML from stdin and send output to a file:

`cat {{path/to/input.xml}} | zek -p -o {{path/to/output.go}}`
