# go list

> Lista pachetelor sau modulelor.
> Mai multe informaţii: <https://golang.org/cmd/go/#hdr-List_packages_or_modules>

- Lista pachetelor:

`go list ./...`

- Lista pachetelor standard:

`go list std`

- Lista pachetelor în format json:

`go list -json time net/http`

- Lista dependențelor modulului și actualizările disponibile:

`go list -m -u all`
