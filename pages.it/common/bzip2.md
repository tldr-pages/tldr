# bzip2

> Compressore di file a blocchi ordinati.
> Vedi anche: `bzcat`, `bunzip2`, `bzip2recover`.
> Maggiori informazioni: <https://manned.org/bzip2>.

- Comprimi un file:

`bzip2 {{percorso/del/file}}`

- Decomprimi un file:

`bzip2 -d {{percorso/del/file_compresso.bz2}}`

- Decomprimi un file e mostrane il contenuto su `stdout`:

`bzip2 -dc {{percorso/del/file_compresso.bz2}}`
