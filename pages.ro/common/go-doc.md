# go doc

> Afișați documentația pentru un pachet sau un simbol.
> Mai multe informaţii: <https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>

- Afișați documentația pentru pachetul curent:

`go doc`

- Afișează documentația pachetului și simbolurile exportate:

`go doc {{encoding/json}}`

- Arată, de asemenea, documentația de simboluri:

`go doc -all {{encoding/json}}`

- Arată, de asemenea, surse:

`go doc -all -src {{encoding/json}}`

- Arată un simbol specific:

`go doc -all -src {{encoding/json.Number}}`
