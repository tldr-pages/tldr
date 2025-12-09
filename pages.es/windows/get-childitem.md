# Get-ChildItem

> Lista los elementos en un directorio.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-childitem>.

- Lista todos los elementos no ocultos en el directorio actual:

`Get-ChildItem`

- Lista solo directorios en el directorio actual:

`Get-ChildItem -Directory`

- Lista solo archivos en el directorio actual:

`Get-ChildItem -File`

- Lista elementos en el directorio actual, incluyendo elementos ocultos:

`Get-ChildItem -Hidden`

- Lista elementos en un directorio diferente al actual:

`Get-ChildItem -Path {{ruta\al\directorio}}`
