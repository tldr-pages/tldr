# Out-String

> Salida de objetos de entrada como una cadena.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-string>.

- Imprimir información del host como cadena:

`Get-Alias | Out-String`

- Convertir cada objeto a una cadena en lugar de concatenar todos los objetos en una sola cadena:

`Get-Alias | Out-String -Stream`

- Usar el parámetro `Width` (Ancho) para evitar la truncación:

`@{TestKey = ('x' * 200)} | Out-String -Width {{250}}`
