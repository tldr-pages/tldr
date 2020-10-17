# Get-Content

> Get the content of the item at the specified location.
> More information: <https://docs.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- Get the content of a file:

`Get-Content -Path {{file_name}}`

- Limit the number of lines returned by Get-Content o conteúdo de um arquivo limitando o numero de linhas:

`Get-Content -Path {{file_name}} -TotalCount {{number_of_lines}}`

- Get the content of the file and keeps it open to print each new line:

`Get-Content -Path {{file_name}} -Wait`
