# 7za

> Archiviatore di file con alto fattore di compressione.
> Versione standalone di `7z` con supporto a meno tipi di archivi.

- Archivia un file o una directory:

`7za a {{archivio.7z}} {{percorso/al/file}}`

- Estrai un archivio mantenendo la gerarchia delle cartelle:

`7za x {{archivio.7z}}`

- Archivia utilizzando uno specifico tipo di archivio:

`7za a -t {{zip|gzip|bzip2|tar|...}} {{archivio.7z}} {{percorso/al/file}}`

- Elenca i tipi di archivio supportati:

`7za i`

- Elenca i contenuti in un archivio:

`7za l {{archivio}}`
