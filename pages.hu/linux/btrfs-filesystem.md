# btrfs filesystem

> A btrfs fájlrendszerek kezelése. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- A fájlrendszer használatának megjelenítése (a részletes információk megjelenítéséhez opcionálisan root-ként futtatható):

`btrfs filesystem usage {{path/to/btrfs_mount}}`

- Megjeleníti az egyes eszközök használatát:

`sudo btrfs filesystem show {{path/to/btrfs_mount}}`

- Egyetlen fájl defragmentálása egy btrfs fájlrendszeren (kerülje el a deduplikációs ügynök futása közben):

`sudo btrfs filesystem defragment -v {{path/to/file}}`

- Könyvtár rekurzív defragmentálása (nem lépi át az alkötetek határait):

`sudo btrfs filesystem defragment -v -r {{path/to/directory}}`

- A meg nem írt adatblokkok szinkronizálásának kikényszerítése a lemez(ek)re:

`sudo btrfs filesystem sync {{path/to/btrfs_mount}}`

- Egy könyvtárban lévő fájlok lemezhasználatának rekurzív összegzése:

`sudo btrfs filesystem du --summarize {{path/to/directory}}`
