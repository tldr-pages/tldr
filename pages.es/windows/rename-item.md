# Rename-Item

> Comando de Powershell para cambiar el nombre de un elemento.
> Nota: Tanto `ren` como `rni` pueden utilizarse como alias de `Rename-Item`.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/rename-item>.

- Cambia el nombre de un archivo:

`Rename-Item -Path "{{ruta\al\archivo}}" -NewName "{{nuevo_nombre_archivo}}"`

- Cambia el nombre de un directorio:

`Rename-Item -Path "{{ruta\al\directorio}}" -NewName "{{nuevo_nombre_directorio}}"`

- Cambia el nombre y mueve un archivo:

`Rename-Item -Path "{{ruta\al\archivo}}" -NewName "{{ruta\al\nuevo_nombre_archivo}}"`

- Cambia el nombre de un archivo de forma forzada:

`Rename-Item -Path "{{ruta\al\archivo}}" -NewName "{{nuevo_nombre_archivo}}" -Force`

- Solicita confirmación antes de cambiar el nombre de un archivo:

`Rename-Item -Path "{{ruta\al\archivo}}" -NewName "{{nuevo_nombre_archivo}}" {{[-Confirm|-cf]}}`
