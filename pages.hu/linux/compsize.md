# compsize

> A btrfs fájlrendszeren lévő fájlok egy halmazának tömörítési arányának kiszámítása. Lásd még: `btrfs filesystem` egy fájl újratömörítéséhez defragmentálással. További információ: <https://github.com/kilobyte/compsize>.

- Egy fájl vagy könyvtár aktuális tömörítési arányának kiszámítása:

`sudo compsize {{path/to/file_or_directory}}`

- Ne lépje át a fájlrendszer határait:

`sudo compsize --one-file-system {{path/to/file_or_directory}}`

- Nyers bájtszámok megjelenítése az ember által olvasható méretek helyett:

`sudo compsize --bytes {{path/to/file_or_directory}}`
