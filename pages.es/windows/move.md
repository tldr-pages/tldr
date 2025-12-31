# move

> Mover o renombrar archivos y directorios.
> En PowerShell, este comando es un alias de `Move-Item`. Esta documentación se basa en la versión de `move` del Símbolo del sistema (`cmd`).
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/move>.

- Ver la documentación del comando equivalente de PowerShell:

`tldr move-item`

- Renombrar un archivo o directorio cuando el destino no es un directorio existente:

`move {{ruta\al\origen}} {{ruta\al\destino}}`

- Mover un archivo o directorio a un directorio existente:

`move {{ruta\al\origen}} {{ruta\al\directorio_existente}}`

- Mover un archivo o directorio entre unidades:

`move {{C:\ruta\al\origen}} {{D:\ruta\al\destino}}`

- No solicitar confirmación antes de sobrescribir archivos existentes:

`move /Y {{ruta\al\origen}} {{ruta\al\directorio_existente}}`

- Solicitar confirmación antes de sobrescribir archivos existentes, independientemente de los permisos de archivo:

`move /-Y {{ruta\al\origen}} {{ruta\al\directorio_existente}}`
