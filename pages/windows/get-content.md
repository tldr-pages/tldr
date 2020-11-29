# Get-Content

> Get the content of the item at the specified location.
> More information: <https://docs.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- Display the content of a file:

`Get-Content -Path {{path/to/file}}`

- Display the first few lines of a file:

`Get-Content -Path {{path/to/file}} -TotalCount {{count}}`

- Display the content of the file and keep reading from it until `Ctrl + C` is pressed:

`Get-Content -Path {{path/to/file}} -Wait`
