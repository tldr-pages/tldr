# Get-Content

> Obtiene el contenido del elemento en la ubicación especificada.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- Muestra el contenido de un archivo:

`Get-Content -Path {{ruta\al\archivo}}`

- Muestra las primeras líneas de un archivo:

`Get-Content -Path {{ruta\al\archivo}} -TotalCount {{10}}`

- Muestra el contenido del archivo y sigue leyendo hasta que se presione `<Ctrl c>`:

`Get-Content -Path {{ruta\al\archivo}} -Wait`
