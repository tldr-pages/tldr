# xzdiff

> Ejecuta `diff` en archivos comprimidos con formatos de compresión `xz`, `lzma`, `gzip`, `bzip2`, `lzop` o `zstd`.
> Todas las opciones especificadas se pasan directamente a `diff`.
> Más información: <https://manned.org/xzdiff>.

- Compara dos archivos:

`xzdiff {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Compara dos archivos, mostrando las diferencias en paralelo:

`xzdiff --side-by-side {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Compara dos archivos e informa solo de que difieren (sin detalles sobre qué es en lo que difiere):

`xzdiff --brief {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Compara dos archivos e informa de cuándo los archivos son iguales:

`xzdiff --report-identical-files {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Compara dos archivos utilizando resultados paginados:

`xzdiff --paginate {{ruta/al/archivo1}} {{ruta/al/archivo2}}`
