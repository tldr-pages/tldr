# 7za

> Archiviatore di file con alto fattore di compressione.
> Versione standalone di `7z` con supporto a meno tipi di archivi.
> Maggiori informazioni: <https://www.7-zip.org>.

- Archivia un file o una cartella:

`7za a {{archivio.7z}} {{percorso/del/file_o_cartella}}`

- Estrai un archivio mantenendo la gerarchia delle cartelle:

`7za x {{archivio.7z}}`

- Archivia utilizzando uno specifico tipo di archivio:

`7za a -t {{zip|gzip|bzip2|tar}} {{archivio.7z}} {{percorso/del/file_o_cartella}}`

- Elenca i tipi di archivio supportati:

`7za i`

- Elenca i contenuti in un archivio:

`7za l {{archivio}}`
