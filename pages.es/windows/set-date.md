# Set-Date

> Cambia la hora del sistema en el equipo a una hora que especifiques.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/set-date>.

- Agregar tres días a la fecha del sistema:

`Set-Date -Date (Get-Date).AddDays({{3}})`

- Retrasar el reloj del sistema 10 minutos:

`Set-Date -Adjust -0:10:0 -DisplayHint Time`

- Agregar 90 minutos al reloj del sistema:

`$90mins = New-TimeSpan -Minutes {{90}}; Set-Date -Adjust $90mins`
