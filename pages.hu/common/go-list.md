# go list

> Csomagok vagy modulok listázása. További információ: <https://golang.org/cmd/go/#hdr-List_packages_or_modules>.

- Csomagok listázása:

`go list ./...`

- Standard csomagok listázása:

`go list std`

- Csomagok listázása JSON formátumban:

`go list -json time net/http`

- Modulfüggőségek és elérhető frissítések listázása:

`go list -m -u all`
