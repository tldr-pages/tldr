# umount

> Egy fájlrendszer függetlenítése a csatolási pontjától, így az nem lesz többé elérhető. Egy fájlrendszert nem lehet függetleníteni, ha az foglalt. További információ: <https://manned.org/umount.8>.

- Egy fájlrendszer leválasztása a forrás elérési útjának átadásával, ahonnan fel van kötve:

`umount {{path/to/device_file}}`

- Egy fájlrendszer leválasztása a célállomás elérési útvonalának megadásával, ahová fel van kötve:

`umount {{path/to/mounted_directory}}`

- Az összes csatlakoztatott fájlrendszer leválasztása (kivéve a `proc` fájlrendszert):

`umount -a`
