# gpgconf

> A .gnupg kezdeti könyvtárak módosítása. További információ: <https://www.gnupg.org/documentation/manuals/gnupg/gpgconf.html>.

- Az összes komponens listázása:

`gpgconf --list-components`

- A gpgconf által használt könyvtárak listázása:

`gpgconf --list-dirs`

- Egy komponens összes opciójának listázása:

`gpgconf --list-options {{component}}`

- Programok listázása és tesztelése, hogy futtathatóak-e:

`gpgconf --check-programs`

- Egy komponens újratöltése:

`gpgconf --reload {{component}}`
