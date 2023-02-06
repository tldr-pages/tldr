# clamdscan

> Parancssori vírusellenőrző a ClamAV Daemon segítségével. További információ: <https://www.clamav.net>.

- Egy fájl vagy könyvtár vizsgálata sebezhetőségek után:

`clamdscan {{path/to/file_or_directory}}`

- Az adatok vizsgálata a `stdin` oldalon:

`{{command}} | clamdscan -`

- Az aktuális könyvtár átvizsgálása és csak a fertőzött fájlok kimenete:

`clamdscan --infected`

- A vizsgálati jelentés kiadása egy naplófájlba:

`clamdscan --log {{path/to/log_file}}`

- Fertőzött fájlok áthelyezése egy adott könyvtárba:

`clamdscan --move {{path/to/quarantine_directory}}`

- Fertőzött fájlok eltávolítása:

`clamdscan --remove`

- Több szál használata egy könyvtár átvizsgálásához:

`clamdscan --multiscan`

- A fájl leírójának átadása a démonnak a fájl streamelése helyett:

`clamdscan --fdpass`
