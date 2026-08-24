# bzip2

> Compresso file con ordinamento a blocchi.
> Vedi anche: `bzcat`, `bunzip2`, `bzip2recover`.
> Maggiori informazioni: <https://manned.org/bzip2>.

- Comprimi un file:

`bzip2 {{percorso/al/file_da_comprimere}}`

- Decomprimi un file:

`bzip2 {{[-d|--decompress]}} {{percorso/al/file_compresso.bz2}}`

- Decomprimi un file su `stdout`:

`bzip2 {{[-dc|--decompress --stdout]}} {{percorso/al/file_compresso.bz2}}`

- Testa l'integrità di ogni file nell'archivio:

`bzip2 {{[-t|--test]}} {{percorso/al/file_compresso.bz2}}`

- Mostra il rapporto di compressione per ogni file con informazioni dettagliate:

`bzip2 {{[-v|--verbose]}} {{percorso/al/file_compresso.bz2}}`

- Decomprimi un file sovrascrivendo i file esistenti:

`bzip2 {{[-f|--force]}} {{percorso/al/file_compresso.bz2}}`

- Visualizza l'aiuto:

`bzip2 {{[-h|--help]}}`
