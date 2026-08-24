# go list

> Elenca pacchetti o moduli.
> Maggiori informazioni: <https://pkg.go.dev/cmd/go#hdr-List_packages_or_modules>.

- Elenca pacchetti:

`go list ./...`

- Elenca pacchetti standard:

`go list std`

- Elenca pacchetti in formato JSON:

`go list -json time net/http`

- Elenca dipendenze moduli e aggiornamenti disponibili:

`go list -m -u all`
