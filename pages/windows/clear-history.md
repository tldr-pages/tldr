# Clear-History

> A powershell command to clear the entries in the current session.
> Note: `clhy` can both be used as an alias for `Clear-History`.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/clear-history>.

- Clear all command history:

`Clear-History`

- Clear command by specific name:

`Clear-History -CommandLine "{{command}}"`

- Clear multiple commands by name:

`Clear-History -CommandLine "{{command_1}}", "{{command_2}}"`

- Clear a specific history entry by ID:

`Clear-History -Id {{id_number}}`

- Clear multiple IDs:

`Clear-History -Id {{id_1}}, {{id_2}}, {{id_3}}`

- Clear commands within a range of IDs:

`Clear-History -Id ({{start_id}}..{{end_id}})`

- Show what would be deleted:

`Clear-History -WhatIf`

- Ask for confirmation before clearing:

`Clear-History -Confirm`
