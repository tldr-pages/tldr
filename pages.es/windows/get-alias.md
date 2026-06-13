# Get-Alias

> Listar y obtener alias de comandos en la sesión actual de PowerShell.
> Este comando solo se puede ejecutar en PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>.

- Listar todos los alias en la sesión actual:

`Get-Alias`

- Obtener el nombre del comando asociado al alias:

`Get-Alias {{alias_de_comando}}`

- Listar todos los alias asignados a un comando específico:

`Get-Alias -Definition {{comando}}`

- Listar alias que comienzan con `abc`, excluyendo aquellos que terminan en `def`:

`Get-Alias {{abc}}* -Exclude *{{def}}`
