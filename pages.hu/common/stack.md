# stack

> Haskell projektek kezelésére szolgáló eszköz. További információ: <https://github.com/commercialhaskell/stack>.

- Új csomag létrehozása:

`stack new {{package_name}} {{template_name}}`

- Csomag összeállítása:

`stack build`

- Tesztek futtatása egy csomagon belül:

`stack test`

- Projekt fordítása és újrakompilálás minden egyes fájlváltoztatáskor:

`stack build --file-watch`

- Egy projekt fordítása és egy parancs végrehajtása a fordítás után:

`stack build --exec "{{command}}"`

- Egy program futtatása és egy argumentum átadása:

`stack exec {{program_name}} -- {{argument}}`
