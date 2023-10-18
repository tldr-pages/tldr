# Resolve-Path

> Resolves the wildcard characters in a path, and displays the path contents.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- Resolve the home folder path:

`Resolve-Path {{~}}`

- Resolve a UNC path:

`Resolve-Path -Path "\\{{hostname}}\{{path\to\file}}"`

- Get relative paths:

`Resolve-Path -Path {{path\to\file_or_directory}} -Relative`
