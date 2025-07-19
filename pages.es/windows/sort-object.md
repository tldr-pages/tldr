# Sort-Object

> Ordena objetos por valores de propiedades.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/sort-object>.

- Ordenar el directorio actual por nombre:

`Get-ChildItem | Sort-Object`

- Ordenar el directorio actual por nombre en orden descendente:

`Get-ChildItem | Sort-Object -Descending`

- Ordenar elementos eliminando duplicados:

`"a", "b", "a" | Sort-Object -Unique`

- Ordenar el directorio actual por tamaño de archivo (longitud):

`Get-ChildItem | Sort-Object -Property Length`

- Ordenar procesos por el uso más alto de memoria basado en su tamaño de conjunto de trabajo (WS):

`Get-Process | Sort-Object -Property WS`
