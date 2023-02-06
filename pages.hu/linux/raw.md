# raw

> Unix nyers karakteres eszköz kötése. További információ: <https://manned.org/raw.8>.

- Nyers karakteres eszköz kötése blokkos eszközhöz:

`raw /dev/raw/raw{{1}} {{/dev/block_device}}`

- Egy meglévő kötés lekérdezése új kötés beállítása helyett:

`raw /dev/raw/raw{{1}}`

- Az összes kötött nyers karakteres eszköz lekérdezése:

`raw -qa`
