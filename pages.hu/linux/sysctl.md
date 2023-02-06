# sysctl

> A kernel futásidejű változóinak listázása és módosítása. További információ: <https://manned.org/sysctl.8>.

- Az összes elérhető változó és értékük megjelenítése:

`sysctl -a`

- Megváltoztatható kernelállapotváltozó beállítása:

`sysctl -w {{section.tunable}}={{value}}`

- Jelenleg nyitott fájlkezelők lekérdezése:

`sysctl fs.file-nr`

- Az egyidejűleg megnyitott fájlok határértékének lekérdezése:

`sysctl fs.file-max`

- A `/etc/sysctl.conf` oldalon végrehajtott változtatások alkalmazása:

`sysctl -p`
