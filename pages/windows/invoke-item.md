# Invoke-Item

> Open files in their respective default programs.
> This command can only be used through PowerShell.
> More information: <https://docs.microsoft.com/powershell/module/microsoft.powershell.management/invoke-item>.

- Open a file in its default program:

`Invoke-Item -Path {{path/to/file}}`

- Open all files inside a directory:

`Invoke-Item -Path {{path/to/directory/*}}`

- Open all PNGs inside a directory:

`Invoke-Item -Path {{path/to/directory/*.png}}`

- Open all files inside a directory containing a specific keyword:

`Invoke-Item -Path {{path/to/directory/*}} -Include {{*keyword*}}`

- Open all files inside a directory except those containing a specific keyword:

`Invoke-Item -Path {{path/to/directory/*}} -Exclude {{*keyword*}}`

- Perform a dry run to determine which files will be opened inside a directory through `Invoke-Item`:

`Invoke-Item -Path {{path/to/directory/*}} -WhatIf`
