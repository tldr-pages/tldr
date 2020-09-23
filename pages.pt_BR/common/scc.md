# scc

> Utilitário escrito em GO que conta linhas de código.
> Mais informações: <https://github.com/boyter/scc>.

- Mostrar o número de linhas de código no diretório atual:

`scc`

- Mostrar o número de linhas de código de um diretório especificado:

`scc {{caminho/para/diretorio}}`

- Mostrar o número de linhas de código por arquivo:

`scc --by-file`

- Mostrar o resultado usando um formato específico (formato padrão é o `tabular`):

`scc --format {{tabular|wide|json|csv|cloc-yaml|html|html-table}}`

- Contar apenas os arquivos com as extensões especificadas:

`scc --include-ext {{go, java, js}}`

- Excluir diretórios da contagem:

`scc --exclude-dir {{.git,.hg}}`

- Mostrar output organizado de acordo com o parâmetro especificado (organização padrão é `files`):

`scc --sort {{files|name|lines|blanks|code|comments|complexity}}`

- Mostra a tela de ajuda:

`scc -h`
