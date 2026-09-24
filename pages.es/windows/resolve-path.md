# Resolve-Path

> Resuelve los caracteres comodín en una ruta y muestra el contenido de la ruta.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- Resolve la ruta de la carpeta de inicio:

`Resolve-Path ~`

- Resolve una ruta UNC:

`Resolve-Path -Path "\\{{nombre_del_host}}\{{ruta\al\archivo}}"`

- Obtene rutas relativas:

`Resolve-Path -Path {{ruta\al\archivo_o_directorio}} -Relative`
