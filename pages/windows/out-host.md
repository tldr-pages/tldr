# Out-Host

> Handle and output `stdout` of any command within PowerShell session.
> Can also be used as a substitute of `more`.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/out-host>.

- Display a command output or variable's value into the command-line (equivalent to invoking the command or variable without `Out-Host` itself):

`{{command_or_variable}} | Out-Host`

- Display the output into an interactive paging view (will not work in PowerShell ISE):

`{{command_or_variable}} | Out-Host -Paging`

- Interactively display a text file within the paging view (equivalent to `more {{path/to/file}}`):

`Get-Content {{path\to\file}} | Out-Host -Paging`

- Go to the next page within the paging view:

`<Space>`

- Go to the next page within the paging view:

`<Enter>`

- Exit the paging view:

`<q>`
