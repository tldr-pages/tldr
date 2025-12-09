# Select-String

> Busca texto en cadenas y archivos en PowerShell.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Puedes usar `Select-String` de manera similar a `grep` en UNIX o `findstr.exe` en Windows.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- Buscar un patrón dentro de un archivo:

`Select-String -Path "{{ruta\al\archivo}}" -Pattern '{{patrón_de_búsqueda}}'`

- Buscar una cadena exacta (desactiva expresiones regulares):

`Select-String -SimpleMatch "{{cadena_exacta}}" {{ruta\al\archivo}}`

- Buscar un patrón en todos los archivos `.ext` en el directorio actual:

`Select-String -Path "{{*.ext}}" -Pattern '{{patrón_de_búsqueda}}'`

- Capturar el número especificado de líneas antes y después de la línea que coincide con el patrón:

`Select-String --Context {{2,3}} "{{patrón_de_búsqueda}}" {{ruta\al\archivo}}`

- Buscar en `stdin` líneas que no coincidan con un patrón:

`Get-Content {{ruta\al\archivo}} | Select-String --NotMatch "{{patrón_de_búsqueda}}"`
