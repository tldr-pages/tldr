# go doc

> Egy csomag vagy szimbólum dokumentációjának megjelenítése. További információ: <https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- Az aktuális csomag dokumentációjának megjelenítése:

`go doc`

- A csomag dokumentációjának és az exportált szimbólumoknak a megjelenítése:

`go doc {{encoding/json}}`

- Mutassa meg a szimbólumok dokumentációját is:

`go doc -all {{encoding/json}}`

- Mutassa meg a forrásokat is:

`go doc -all -src {{encoding/json}}`

- Egy adott szimbólum megjelenítése:

`go doc -all -src {{encoding/json.Number}}`
