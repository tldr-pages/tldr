# Clear-History

> Delete entries from the PowerShell session command history.
> Note: `clhy` can be used as an alias for `Clear-History`.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/clear-history>.

- Clear all command history from current session:

`Clear-History`

- Clear command by specific name:

`Clear-History -CommandLine "{{command}}"`

- Clear multiple commands by name:

`Clear-History -CommandLine {{"command1", "command2", ...}}`

- Clear a specific history entry by ID:

`Clear-History -Id {{id_number}}`

- Clear multiple IDs:

`Clear-History -Id {{id1, id2, ...}}`

- Clear commands within a range of IDs:

`Clear-History -Id ({{start_id}}..{{end_id}})`

- Show what would be deleted:

`Clear-History -WhatIf`

- Ask for confirmation before clearing:

`Clear-History -Confirm`
