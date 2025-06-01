# Get-Date

> Obtiene la fecha y hora actuales.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- Muestra la fecha y hora actuales:

`Get-Date`

- Muestra la fecha y hora actuales con un especificador de formato .NET:

`Get-Date -Format "{{yyyy-MM-dd HH:mm:ss}}"`

- Muestra la fecha y hora actuales en UTC y en formato ISO 8601:

`(Get-Date).ToUniversalTime()`

- Convierte un timestamp de Unix:

`Get-Date -UnixTimeSeconds {{1577836800}}`
