# 7zr

> Archiviatore di file con alto rapporto di compressione.
> Simile a `7z` ma supporta solo file 7z.
> Maggiori informazioni: <https://manned.org/7zr>.

- [a]rchivia un file o directory:

`7zr a {{percorso/all/archivio.7z}} {{percorso/al/file_o_directory}}`

- Crittografa un archivio esistente (inclusi i nomi dei file):

`7zr a {{percorso/all/archivio_crittografato.7z}} -p{{password}} -mhe={{on}} {{percorso/all/archivio.7z}}`

- Estrai un archivio preservando la struttura delle directory originali:

`7zr x {{percorso/all/archivio.7z}}`

- Estrai un archivio in una directory specifica:

`7zr x {{percorso/all/archivio.7z}} -o{{percorso/all/output}}`

- Estrai un archivio su `stdout`:

`7zr x {{percorso/all/archivio.7z}} -so`

- [l]istai i contenuti di un archivio:

`7zr l {{percorso/all/archivio.7z}}`

- Imposta il livello di compressione (più alto = maggiore compressione ma più lento):

`7zr a {{percorso/all/archivio.7z}} -mx={{0|1|3|5|7|9}} {{percorso/al/file_o_directory}}`
