# del

> Elimina uno o más archivos.
> En PowerShell, este comando es un alias de `Remove-Item`. Esta documentación se basa en la versión del símbolo del sistema (`cmd`) de `del`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Muestra la documentación del comando PowerShell equivalente:

`tldr remove-item`

- Elimina uno o más archivos o patrones separados por espacios:

`del {{patrón_del_archivo}}`

- Solicita confirmación antes de borrar cada archivo:

`del {{patrón_del_archivo}} /p`

- Fuerza la eliminación de archivos de sólo lectura:

`del {{patrón_del_archivo}} /f`

- Elimina recursivamente archivos de todos los subdirectorios:

`del {{patrón_del_archivo}} /s`

- Elimina archivos que coincidan con un comodín sin confirmación:

`del {{patrón_del_archivo}} /q`

- Muestra la ayuda y la lista de atributos disponibles:

`del /?`

- Elimina archivos en función de los atributos especificados:

`del {{patrón_del_archivo}} /a {{atributo}}`
