# kate

> Editor de texto avançado do KDE.
> Mais informações: <https://kate-editor.org/>.

- Abre arquivos específicos:

`kate {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`

- Abre arquivos remotos específicos:

`kate {{https://example.com/caminho/para/arquivo1 https://example.com/caminho/para/arquivo2 ...}}`

- Cria uma uma nova instância do editor mesmo que uma já esteja aberta:

`kate --new`

- Abre um arquivo com o cursor em uma linha específica:

`kate --line {{número_linha}} {{caminho/para/arquivo}}`

- Abre um arquivo com o cursor em uma linha e coluna específica:

`kate --line {{número_linha}} --column {{número_coluna}} {{caminho/para/arquivo}}`

- Cria um arquivo a partir do `stdin`:

`cat {{caminho/para/arquivo}} | kate --stdin`

- Exibe ajuda:

`kate --help`
