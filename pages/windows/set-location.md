# Set-Location

> Display the current working directory or move to a different directory.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Go to the specified directory:

`Set-Location {{path\to\directory}}`

- Go to a specific directory in a different drive:

`Set-Location {{C}}:{{path\to\directory}}`

- Go and display the location of specified directory:

`Set-Location {{path\to\directory}} -PassThru`

- Go up to the parent of the current directory:

`Set-Location ..`

- Go to the home directory of the current user:

`Set-Location ~`

- Go back/forward to the previously chosen directory:

`Set-Location {{-|+}}`

- Go to root of current drive:

`Set-Location \`
