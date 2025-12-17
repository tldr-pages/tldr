# Clear-History

> Elimina las entradas del historial de comandos de la sesión de PowerShell.
> Nota: `clhy` se puede utilizar como alias de `Clear-History`.
> Más información: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/clear-history>.

- Borra todo el historial de comandos de la sesión actual:

`Clear-History`

- Borra un comando por su nombre específico:

`Clear-History -CommandLine "{{comando}}"`

- Borra varios comandos por su nombre:

`Clear-History -CommandLine {{"comando1", "comando2", ...}}`

- Borra una entrada específica del historial por ID:

`Clear-History -Id {número_id}`

- Borra varios ID:

`Clear-History -Id {id1, id2, ...}`

- Borra comandos dentro de un rango de IDs:

`Clear-History -Id ({{id_inicial}}..{{id_final}})`

- Muestra lo que se eliminaría:

`Clear-History -WhatIf`

- Pide confirmación antes de borrar:

`Clear-History -Confirm`
