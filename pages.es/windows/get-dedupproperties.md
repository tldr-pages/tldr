# Get-DedupProperties

> Obtiene información sobre la desduplicación de datos.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/storage/get-dedupproperties>.

- Obtiene información sobre la desduplicación de datos de la unidad:

`Get-DedupProperties -DriveLetter 'C'`

- Obtiene información sobre la desduplicación de datos de la unidad utilizando la etiqueta de la unidad:

`Get-DedupProperties -FileSystemLabel 'Etiqueta'`

- Obtiene información sobre la desduplicación de datos de la unidad utilizando el objeto de entrada:

`Get-DedupProperties -InputObject $(Get-Volume -DriveLetter 'E')`
