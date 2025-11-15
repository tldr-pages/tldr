# 7za

> Archiviatore di file con alto fattore di compressione.
> Versione standalone di `7z` con supporto a meno tipi di archivi.
> Maggiori informazioni: <https://manned.org/7za>.

- Archivia un file o una directory:

`7za a {{archivio.7z}} {{percorso/del/file_o_directory}}`

- Estrai un archivio mantenendo la gerarchia delle directory:

`7za x {{archivio.7z}}`

- Archivia utilizzando uno specifico tipo di archivio:

`7za a -t {{zip|gzip|bzip2|tar}} {{archivio.7z}} {{percorso/del/file_o_directory}}`

- Elenca i contenuti in un archivio:

`7za l {{archivio}}`
