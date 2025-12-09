# join

> Junta linhas de dois arquivos ordenados em um campo comum.
> Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html>.

- Junta dois arquivos no primeiro campo (padrão):

`join {{caminho/para/arquivo1}} {{caminho/para/arquivo2}}`

- Junta dois arquivos usando uma vírgula (em vez de um espaço) como separador de campo:

`join -t {{','}} {{caminho/para/arquivo1}} {{caminho/para/arquivo2}}`

- Junta campo3 do arquivo1 ao campo1 do arquivo2:

`join -1 {{3}} -2 {{1}} {{caminho/para/arquivo1}} {{caminho/para/arquivo2}}`

- Produz uma linha para cada linha que não pode ser pareada para o arquivo1:

`join -a {{1}} {{caminho/para/arquivo1}} {{caminho/para/arquivo2}}`

- Junta aquivo da entrada padrão (`stdin`):

`cat {{caminho/para/arquivo1}} | join - {{caminho/para/arquivo2}}`
