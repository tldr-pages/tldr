# Clear-RecycleBin

> Elimina elementos de la Papelera de reciclaje.
> Este comando solo se puede usar a través de PowerShell versiones 5.1 y anteriores, o 7.1 y posteriores.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.

- Limpia y eliminar todos los elementos dentro de la Papelera de reciclaje:

`Clear-RecycleBin`

- Limpia la Papelera de reciclaje para una unidad específica:

`Clear-RecycleBin -DriveLetter {{C}}`

- Limpia la Papelera de reciclaje sin más confirmación:

`Clear-RecycleBin -Force`
