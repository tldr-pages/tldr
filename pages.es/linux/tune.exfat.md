# tune.exfat

> Ajusta los parámetros del sistema de archivos en un sistema de archivos exFAT.
> Más información: <https://manned.org/tune.exfat>.

- Imprime la etiqueta de volumen de un sistema de archivos:

`tune.exfat {{[-l|--print-label]}} {{/dev/sdXY}}`

- Establece la etiqueta de volumen de un sistema de archivos:

`tune.exfat {{[-L|--set-label]}} {{nueva_etiqueta}} {{/dev/sdXY}}`

- Imprime el GUID del volumen de un sistema de archivos:

`tune.exfat {{[-u|--print-guid]}} {{/dev/sdXY}}`

- Establece el GUID de volumen de un sistema de archivos:

`tune.exfat {{[-U|--set-guid]}} {{nuevo_guid}} {{/dev/sdXY}}`

- Imprime el número de serie del volumen de un sistema de archivos:

`tune.exfat {{[-i|--print-serial]}} {{/dev/sdXY}}`

- Establece el volumen de serie de un sistema de archivos:

`tune.exfat {{[-I|--set-serial]}} {{nuevo_serial}} {{/dev/sdXY}}`
