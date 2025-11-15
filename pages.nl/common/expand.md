# expand

> Vervang tabs met spaties.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/expand-invocation.html>.

- Vervang tabs in ieder bestand met spaties en schrijf het naar `stdout`:

`expand {{pad/naar/bestand}}`

- Vervang tabs met spaties, lezend vanaf `stdin`:

`expand`

- Vervang geen tabs na een karakter:

`expand {{[-i|--initial]}} {{pad/naar/bestand}}`

- Laat tabs een bepaald aantal tekens uit elkaar staan, niet 8:

`expand {{[-t|--tabs]}} {{nummer}} {{pad/naar/bestand}}`

- Gebruik een door komma's gescheiden lijst met expliciete tabposities:

`expand {{[-t|--tabs]}} {{1,4,6}}`
