# Move-Item

> Mueve o renombra archivos, directorios, claves del registro y otros elementos de datos de PowerShell.
> Este comando solo se puede ejecutar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/move-item>.

- Renombra un archivo o directorio cuando el destino no es un directorio existente:

`Move-Item {{ruta\al\origen}} {{ruta\al\destino}}`

- Mueve un archivo o directorio a un directorio existente:

`Move-Item {{ruta\al\origen}} {{ruta\al\directorio_existente}}`

- Renombra o mueve archivo(s) con un nombre específico (no trata caracteres especiales dentro de cadenas):

`Move-Item -LiteralPath "{{ruta\al\origen}}" {{ruta\al\archivo_o_directorio}}`

- Mueve múltiples archivos a un directorio existente, manteniendo los nombres de archivo sin cambios:

`Move-Item {{ruta\al\origen1 , ruta\al\origen2 ...}} {{ruta\al\directorio_existente}}`

- Mueve o renombra clave(s) del registro:

`Move-Item {{ruta\al\clave_origen1 , ruta\al\clave_origen2 ...}} {{ruta\al\clave_nueva_o_existente}}`

- No solicitar confirmación antes de sobrescribir archivos o claves del registro existentes:

`mv -Force {{ruta\al\origen}} {{ruta\al\destino}}`

- Solicitar confirmación antes de sobrescribir archivos existentes, independientemente de los permisos de archivo:

`mv -Confirm {{ruta\al\origen}} {{ruta\al\destino}}`

- Mueve archivos en modo de simulación, mostrando archivos y directorios que podrían ser movidos sin ejecutarlos:

`mv -WhatIf {{ruta\al\origen}} {{ruta\al\destino}}`
