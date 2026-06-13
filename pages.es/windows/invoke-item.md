# Invoke-Item

> Abre archivos en sus respectivos programas predeterminados.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/invoke-item>.

- Abre un archivo en su programa predeterminado:

`Invoke-Item -Path {{ruta\al\archivo}}`

- Abre todos los archivos dentro de un directorio:

`Invoke-Item -Path {{ruta\al\directorio}}\*`

- Abre todos los PNG dentro de un directorio:

`Invoke-Item -Path {{ruta\al\directorio}}\*.png`

- Abre todos los archivos dentro de un directorio que contengan una palabra clave específica:

`Invoke-Item -Path {{ruta\al\directorio}}\* -Include {{*palabra_clave*}}`

- Abre todos los archivos dentro de un directorio excepto aquellos que contengan una palabra clave específica:

`Invoke-Item -Path {{ruta\al\directorio}}\* -Exclude {{*palabra_clave*}}`

- Realiza una simulación para determinar qué archivos se abrirán dentro de un directorio a través de `Invoke-Item`:

`Invoke-Item -Path {{ruta\al\directorio}}\* -WhatIf`
