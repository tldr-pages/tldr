# scc

> Utilitário escrito em GO que conta linhas de código.
> Mais informações: <https://github.com/boyter/scc>.

- Mostra o número de linhas de código no diretório atual:

`scc`

- Mostra o número de linhas de código de um diretório especificado:

`scc {{caminho/para/diretorio}}`

- Mostra o número de linhas de código por arquivo:

`scc --by-file`

- Mostra o resultado usando um formato específico (formato padrão é o `tabular`):

`scc --format {{tabular|wide|json|csv|cloc-yaml|html|html-table}}`

- Conta apenas os arquivos com as extensões especificadas:

`scc --include-ext {{go, java, js}}`

- Exclui diretórios da contagem:

`scc --exclude-dir {{.git,.hg}}`

- Mostra output organizado de acordo com o parâmetro especificado (organização padrão é `files`):

`scc --sort {{files|name|lines|blanks|code|comments|complexity}}`

- Mostra a tela de ajuda:

`scc -h`
