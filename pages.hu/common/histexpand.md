# history expansion

> A `sh`, `bash`, `zsh`, `rbash` és `ksh` héjak történetének újrafelhasználása és bővítése. További információ: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Futtassa az előző parancsot root-ként (`!!` helyébe az előző parancs lép):

`sudo !!`

- Futtasson egy parancsot az előző parancs utolsó argumentumával:

`{{command}} !$`

- Futtasson egy parancsot az előző parancs első argumentumával:

`{{command}} !^`

- Az előzmények N-edik parancsának futtatása:

`!{{n}}`

- A `n` parancs futtatása az előzményekben a sorokkal hátrébb:

`!-{{n}}`

- A legutolsó olyan parancs futtatása, amely tartalmazza a `string` parancsot:

`!?{{string}}?`

- Az előző parancs futtatása, a `string1` parancsot a `string2` parancsra cserélve:

`^{{string1}}^{{string2}}^`

- Az előzmények kibővítése, de a futtatandó parancsot kiírja ahelyett, hogy ténylegesen futtatná:

`{{!-n}}:p`
