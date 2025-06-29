# Where-Object

> Selecciona objetos de una colección basándose en los valores de sus propiedades.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- Filtrar alias por su nombre:

`Get-Alias | Where-Object -{{Propiedad}} {{Nombre}} -{{eq}} {{nombre}}`

- Listar todos los servicios que están detenidos actualmente. La variable automática `$_` representa cada objeto que se pasa al cmdlet `Where-Object`:

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- Usar múltiples condiciones:

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
