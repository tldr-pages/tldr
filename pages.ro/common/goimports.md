# goimports

> Actualizări Accesați liniile de import, adăugând cele lipsă și eliminând cele nereferențiate.
> Mai multe informaţii: <https://godoc.org/golang.org/x/tools/cmd/goimports>

- Afișează fișierul sursă de import completat:

`goimports {{file}}.go`

- Scrieți rezultatul înapoi în fișierul sursă în locul ieșirii standard:

`goimports -w {{file}}.go`

- Afișează diffs și scrie rezultatul înapoi la fișierul sursă:

`goimports -w -d {{file}}.go`

- Setați șirul prefixului de import după pachetele terțe părți (listă separată prin virgulă):

`goimports -local {{path/to/package}} {{file}}.go`
