# Measure-Command

> Mide el tiempo que tarda en ejecutarse bloques de script y cmdlets.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-command>.

- Mide el tiempo que tarda en ejecutarse un comando:

`Measure-Command { {{comando}} }`

- Pasa la entrada a Measure-Command (los objetos que se pasan a `Measure-Command` están disponibles para el bloque de script que se pasa al parámetro Expression):

`10, 20, 50 | Measure-Command -Expression { for ($i=0; $i -lt $_; $i++) {$i} }`
