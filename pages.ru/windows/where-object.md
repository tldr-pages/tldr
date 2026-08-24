# Where-Object

> Выбирать объекты из коллекции на основе значений их свойств.
> Примечание: эта команда доступна только в PowerShell.
> Больше информации: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- Отфильтровать псевдонимы по имени:

`Get-Alias | Where-Object -{{Property}} {{Name}} -{{eq}} {{имя}}`

- Вывести список всех остановленных служб. Автоматическая переменная `$_` представляет каждый объект, переданный командлету `Where-Object`:

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- Использовать несколько условий:

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
