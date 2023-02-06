# transmission-remote

> Távvezérlő segédprogram a transmission-daemon és a transmission számára. További információ: <https://transmissionbt.com>.

- Torrent fájl vagy mágneses link hozzáadása a Transmissionhez és letöltés egy megadott könyvtárba:

`transmission-remote {{hostname}} -a {{torrent|url}} -w {{/path/to/download_directory}}`

- Az alapértelmezett letöltési könyvtár megváltoztatása:

`transmission-remote {{hostname}} -w {{/path/to/download_directory}}`

- Az összes torrent listázása:

`transmission-remote {{hostname}} --list`

- Az 1. és 2. torrent elindítása, a 3. torrent leállítása:

`transmission-remote {{hostname}} -t "{{1,2}}" --start -t {{3}} --stop`

- Az 1. és 2. torrent eltávolítása, valamint a 2. torrent helyi adatainak törlése:

`transmission-remote {{hostname}} -t {{1}} --remove -t {{2}} --remove-and-delete`

- Az összes torrent leállítása:

`transmission-remote {{hostname}} -t {{all}} --stop`

- Az 1-10. és 15-20. torrentek áthelyezése egy új könyvtárba (amely létrejön, ha nem létezik):

`transmission-remote {{hostname}} -t "{{1-10,15-20}}" --move {{/path/to/new_directory}}`
