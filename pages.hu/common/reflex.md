# reflex

> Eszköz egy könyvtár megfigyelésére és egy parancs újbóli futtatására, ha bizonyos fájlok megváltoznak. További információ: <https://github.com/cespare/reflex>.

- Újraépítés a `make` segítségével, ha bármelyik fájl változik:

`reflex make`

- Go alkalmazás fordítása és futtatása, ha bármelyik `.go` fájl változik:

`reflex --regex='{{\.go$}}' {{go run .}}`

- Egy könyvtár figyelmen kívül hagyása a változások figyelése során:

`reflex --inverse-regex='{{^dir/}}' {{command}}`

- Futtassa a parancsot, amikor a reflex elindul és újraindul a fájlváltozásokra:

`reflex --start-service=true {{command}}`

- A megváltozott fájlnevet helyettesíti:

`reflex -- echo {}`
