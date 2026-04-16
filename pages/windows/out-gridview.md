# Out-GridView

> Display command outputs and objects into an interactive GUI window, allowing scrolling and search.
> Supports parsing columns from PowerShell objects, and interactive filtering of `stdout` to be passed through `stdin`.
> Note: This command can only be used through PowerShell and only within Windows.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-gridview>.

- Display the command or cmdlet outputs into a new window:

`{{command}} | Out-GridView`

- Display a PowerShell hashtable (such as `$PSVersionTable`), and do not finish the command until the window has been closed:

`$PSVersionTable | Out-GridView -Wait`

- Read and parse a CSV file into a new window, with a custom title:

`Import-Csv {{path\to\file.csv}} | Out-GridView -Title {{title}}`

- Interactively select a subset of rows from a previous command's `stdout` to the `stdin` input for another command (use <Shift LeftClick>, <Shift ArrowUp>, or <Shift ArrowDown> to select multiple rows):

`{{previous_command}} | Out-GridView -PassThru | {{next_command}}`

- Interactively select a subset of rows of a text file to be passed as an input for another command:

`Get-Content {{path\to\file.txt}} | Out-GridView -PassThru | {{command}}`
