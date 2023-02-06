# fish

> A Friendly Interactive SHell, egy felhasználóbarátnak tervezett parancssori értelmező. További információ: <https://fishshell.com>.

- Interaktív shell munkamenet indítása:

`fish`

- Interaktív shell munkamenet indítása az indítási konfigurációk betöltése nélkül:

`fish --no-config`

- Konkrét parancsok végrehajtása:

`fish --command "{{echo 'fish is executed'}}"`

- Egy adott szkript végrehajtása:

`fish {{path/to/script.fish}}`

- Egy adott szkript ellenőrzése szintaktikai hibák szempontjából:

`fish --no-execute {{path/to/script.fish}}`

- Konkrét parancsok végrehajtása a `stdin` oldalról:

`{{echo "echo 'fish is executed'"}} | fish`

- Interaktív shell munkamenet indítása privát módban, ahol a shell nem fér hozzá a régi előzményekhez, és nem ment el új előzményeket:

`fish --private`

- Olyan környezeti változó definiálása és exportálása, amely a héj újraindításakor is megmarad (beépített):

`set --universal --export {{variable_name}} {{variable_value}}`
