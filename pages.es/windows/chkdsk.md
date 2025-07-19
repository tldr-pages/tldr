# chkdsk

> Verifica el sistema de archivos y los metadatos del volumen en busca de errores.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Especificar la letra de la unidad (seguida de dos puntos), el punto de montaje o el nombre del volumen a verificar:

`chkdsk {{volumen}}`

- Corregir errores en un volumen específico:

`chkdsk {{volumen}} /f`

- Desmontar un volumen específico antes de verificar:

`chkdsk {{volumen}} /x`

- Cambiar el tamaño del archivo de registro al tamaño especificado (solo para NTFS):

`chkdsk /l{{tamaño}}`
