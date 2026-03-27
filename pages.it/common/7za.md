# 7za

> Archiviatore di file con alto rapporto di compressione.
> Simile a `7z` ma supporta meno tipi di file ed è multipiattaforma.
> Maggiori informazioni: <https://manned.org/7za>.

- [a]rchivia un file o directory:

`7za a {{percorso/all/archivio.7z}} {{percorso/al/file_o_directory}}`

- Crittografa un archivio esistente (inclusi i nomi dei file):

`7za a {{percorso/all/archivio_crittografato.7z}} -p{{password}} -mhe=on {{percorso/all/archivio.7z}}`

- Estrai un archivio preservando la struttura delle directory originali:

`7za x {{percorso/all/archivio.7z}}`

- Estrai un archivio in una directory specifica:

`7za x {{percorso/all/archivio.7z}} -o{{percorso/all/output}}`

- Estrai un archivio su `stdout`:

`7za x {{percorso/all/archivio.7z}} -so`

- [a]rchivia usando un tipo di archivio specifico:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{percorso/all/archivio.7z}} {{percorso/al/file_o_directory}}`

- [l]ista i contenuti di un archivio:

`7za l {{percorso/all/archivio.7z}}`

- Imposta il livello di compressione (più alto = maggiore compressione ma più lento):

`7za a {{percorso/all/archivio.7z}} -mx={{0|1|3|5|7|9}} {{percorso/al/file_o_directory}}`
