# alias

> Aliasokat hoz létre -- olyan szavakat, amelyeket egy parancssorozattal helyettesít. Az aliasok az aktuális héj munkamenettel együtt lejárnak, hacsak nem a héj konfigurációs fájljában vannak definiálva, pl. `~/.bashrc`. További információ: <https://tldp.org/LDP/abs/html/aliases.html>.

- Az összes alias listázása:

`alias`

- Általános alias létrehozása:

`alias {{word}}="{{command}}"`

- Az adott aliashoz tartozó parancs megtekintése:

`alias {{word}}`

- Alias parancs eltávolítása:

`unalias {{word}}`

- A `rm` interaktív paranccsá alakítása:

`alias {{rm}}="{{rm --interactive}}"`

- A `la` létrehozása a `ls --all` parancs rövidítéseként:

`alias {{la}}="{{ls --all}}"`
