# scalafmt

> Kódformázó a Scala számára. A konfigurációkat a `.scalafmt.conf` fájlban tárolja. További információ: <https://scalameta.org/scalafmt>.

- Az aktuális könyvtárban lévő összes `.scala` fájl rekurzív átformázása:

`scalafmt`

- Bizonyos fájlok vagy könyvtárak újraformázása egyéni formázási konfigurációval:

`scalafmt --config {{path/to/.scalafmt.conf}} {{path/to/file_or_directory}} {{path/to/file_or_directory}} {{...}}`

- Ellenőrizze, hogy a fájlok helyesen vannak-e formázva, a `0` visszatérése, ha minden fájl tiszteletben tartja a formázási stílust:

`scalafmt --config {{path/to/.scalafmt.conf}} --test`

- Fájlok vagy könyvtárak kizárása:

`scalafmt --exclude {{path/to/file_or_directory}} {{...}}`

- Csak az aktuális Git-ággal szemben szerkesztett fájlok formázása:

`scalafmt --config {{path/to/.scalafmt.conf}} --mode diff`
