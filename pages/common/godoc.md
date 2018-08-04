# godoc

> Show documentation for go packages.

- Display help for package "fmt":

`godoc {{fmt}}`

- Display help for the function "Printf" of "fmt" package:

`godoc {{fmt}} {{Printf}}`

- Serve documentation as a web server on port "6060":

`godoc -http=:{{6060}}`

- Create an index file:

`godoc -write_index -index_files={{path/to/file}}`

- Use the index file to enable search through the documentation:

`godoc -http=:{{6060}} -index -index_files={{path/to/file}}`
