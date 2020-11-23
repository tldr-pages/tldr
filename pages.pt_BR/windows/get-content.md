# Get-Content

> Exibir o conteúdo de um arquivo.
> Mais informações: <https://docs.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- Exibir o conteúdo de um arquivo:

`Get-Content -Path {{caminho/para/arquivo}}`

- Exibir o conteúdo de um arquivo limitando o numero de linhas:

`Get-Content -Path {{caminho/para/arquivo}} -TotalCount {{limite_de_linhas}}`

- Exibir o conteúdo de um arquivo e mantê-lo aberto para que novos dados sejam exibidos:

`Get-Content -Path {{caminho/para/arquivo}} -Wait`
