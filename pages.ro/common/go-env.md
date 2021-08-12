# go env

> Gestionați variabilele de mediu utilizate de lanțul de instrumente Go.
> Mai multe informaţii: <https://golang.org/cmd/go/#hdr-Print_Go_environment_information>

- Afișează toate variabilele de mediu:

`go env`

- Afișează o variabilă specifică de mediu:

`go env {{GOPATH}}`

- Setați o variabilă de mediu la o valoare:

`go env -w {{GOBIN}}={{path/to/directory}}`

- Resetați valoarea unei variabile de mediu:

`go env -u {{GOBIN}}`
