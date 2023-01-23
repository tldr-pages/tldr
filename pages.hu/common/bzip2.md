# bzip2

> Blokkrendező fájlkompresszor. További információ: <https://manned.org/bzip2>.

- Egy fájl tömörítése:

`bzip2 {{path/to/file_to_compress}}`

- Egy fájl kitömörítése:

`bzip2 -d {{path/to/compressed_file.bz2}}`

- Egy fájl dekompressziója a szabványos kimenetre:

`bzip2 -dc {{path/to/compressed_file.bz2}}`

- Az archívumfájlon belüli egyes fájlok integritásának tesztelése:

`bzip2 --test {{path/to/compressed_file.bz2}}`

- Minden egyes feldolgozott fájl tömörítési arányának megjelenítése részletes információkkal:

`bzip2 --verbose {{path/to/compressed_files.bz2}}`

- A meglévő fájlokat felülíró tömörítés visszafejtése:

`bzip2 --force {{path/to/compressed_file.bz2}}`

- Súgó megjelenítése:

`bzip2 -h`
