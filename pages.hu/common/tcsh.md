# tcsh

> C héj fájlnév-kiegészítéssel és parancssori szerkesztéssel. Lásd még: `csh`. További információ: <https://manned.org/tcsh>.

- Interaktív shell munkamenet indítása:

`tcsh`

- Interaktív shell munkamenet indítása az indítási konfigurációk betöltése nélkül:

`tcsh -f`

- Konkrét \[c\]ommandók végrehajtása:

`tcsh -c "{{echo 'tcsh is executed'}}"`

- Egy adott szkript végrehajtása:

`tcsh {{path/to/script.tcsh}}`

- Egy adott szkript ellenőrzése szintaktikai hibák szempontjából:

`tcsh -n {{path/to/script.tcsh}}`

- Konkrét parancsok végrehajtása a `stdin` oldalról:

`{{echo "echo 'tcsh is executed'"}} | tcsh`
