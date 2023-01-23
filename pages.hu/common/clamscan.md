# clamscan

> Parancssori víruskereső. További információ: <https://www.clamav.net>.

- Egy fájl vizsgálata sebezhetőségek után:

`clamscan {{path/to/file}}`

- Egy adott könyvtár összes fájljának rekurzív vizsgálata:

`clamscan -r {{path/to/directory}}`

- Az adatok vizsgálata a `stdin` oldalon:

`{{command}} | clamscan -`

- Adjon meg egy vírusadatbázis fájlt vagy fájlkönyvtárat:

`clamscan --database {{path/to/database_file_or_directory}}`

- Az aktuális könyvtár átvizsgálása és csak a fertőzött fájlok kimenete:

`clamscan --infected`

- A vizsgálati jelentés kiadása egy naplófájlba:

`clamscan --log {{path/to/log_file}}`

- Fertőzött fájlok áthelyezése egy adott könyvtárba:

`clamscan --move {{path/to/quarantine_directory}}`

- Fertőzött fájlok eltávolítása:

`clamscan --remove yes`
