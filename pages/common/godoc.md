# godoc

> Show documentation for go packages.

- Display help for package "fmt":

`godoc {{fmt}}`

- Display help for the function "Printf" of "fmt" package:

`godoc {{fmt}} {{Printf}}`

- Serve documentation as a web server on port "6060":

`godoc -http=:{{6060}}`
