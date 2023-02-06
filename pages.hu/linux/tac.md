# tac

> Megjeleníti és összekapcsolja a fájlokat fordított sorrendben lévő sorokkal. Lásd még: `cat`. További információ: <https://www.gnu.org/software/coreutils/tac>.

- Bizonyos fájlok fordított sorrendben történő összekapcsolása:

`tac {{path/to/file1 path/to/file2 ...}}`

- A `stdin` fordított sorrendben történő megjelenítése:

`{{cat path/to/file}} | tac`

- Speciális elválasztójel használata:

`tac --separator {{,}} {{path/to/file1 path/to/file2 ...}}`

- Egy adott regex használata elválasztóként:

`tac --regex --separator {{[,;]}} {{path/to/file1 path/to/file2 ...}}`

- Használjon elválasztójelet minden fájl előtt:

`tac --before {{path/to/file1 path/to/file2 ...}}`
