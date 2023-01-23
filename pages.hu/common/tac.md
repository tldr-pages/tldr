# tac

> Megjeleníti és összekapcsolja a fájlokat fordított sorrendben lévő sorokkal. Lásd még: `cat`. További információ: <https://www.gnu.org/software/coreutils/tac>.

- Bizonyos fájlok fordított sorrendben történő összekapcsolása:

`tac {{path/to/file1 path/to/file2 ...}}`

- A `stdin` fordított sorrendben történő megjelenítése:

`{{cat path/to/file}} | tac`

- Konkrét \[s\]eparátor használata:

`tac -s {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Egy adott \[r\]egex használata \[s\]eparátorként:

`tac -r -s {{separator}} {{path/to/file1 path/to/file2 ...}}`

- Használjon elválasztójelet minden fájl előtt:

`tac -b {{path/to/file1 path/to/file2 ...}}`
