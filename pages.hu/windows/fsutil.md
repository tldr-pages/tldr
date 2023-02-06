# fsutil

> Megjeleníti a fájlrendszer köteteire vonatkozó információkat. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil>.

- A kötetek listájának megjelenítése:

`fsutil volume list`

- Egy kötet fájlrendszerére vonatkozó információk megjelenítése:

`fsutil fsInfo volumeInfo {{drive_letter|volume_path}}`

- A fájlrendszer automatikus javításának aktuális állapotának megjelenítése az összes kötet esetében:

`fsutil repair state`

- Az összes kötet piszkos bit állapotának megjelenítése:

`fsutil dirty query`

- Egy kötet piszkos bit állapotának beállítása:

`fsutil dirty set {{drive_letter|volume_path}}`
