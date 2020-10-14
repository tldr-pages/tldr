# Get-Content

> Exibir o conteúdo de um arquivo.
> Mais informações: <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content?view=powershell-7>.

- Exibir o conteúdo de um arquivo:

`Get-Content -Path {{nome_do_arquivo}}`

- Exibir o conteúdo de um arquivo limitando o numero de linhas:

`Get-Content -Path {{nome_do_arquivo}} -TotalCount {{limite_de_linhas}}`

- Exibir o conteúdo de um arquivo e mantê-lo aberto para que novos dados sejam exibidos:

`Get-Content -Path {{nome_do_arquivo}} -Wait`
