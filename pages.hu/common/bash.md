# bash

> Bourne-Again SHell, egy `sh`-kompatibilis parancssori értelmező. Lásd még: `zsh`, `histexpand` (history expansion). További információ: <https://gnu.org/software/bash/>.

- Interaktív shell munkamenet indítása:

`bash`

- Interaktív shell munkamenet indítása az indítási konfigurációk betöltése nélkül:

`bash --norc`

- Konkrét \[c\]ommandók végrehajtása:

`bash -c "{{echo 'bash is executed'}}"`

- Egy adott szkript végrehajtása:

`bash {{path/to/script.sh}}`

- Egy adott szkript végrehajtása, miközben minden egyes parancsot kinyomtat a végrehajtás előtt:

`bash -x {{path/to/script.sh}}`

- Egy adott szkript végrehajtása és megállítás az első \[e\]rror esetén:

`bash -e {{path/to/script.sh}}`

- Konkrét parancsok végrehajtása a `stdin` oldalról:

`{{echo "echo 'bash is executed'"}} | bash`
