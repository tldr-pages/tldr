# ditto

> Copia arquivos e diretórios.
> Mais informações: <https://ss64.com/osx/ditto.html>.

- Sobrescreve o conteúdo do diretório de destino pelo conteúdo do diretório de origem:

`ditto {{caminho/para/origem}} {{caminho/para/destino}}`

- Imprime uma linha na janela do Terminal para cada arquivo que está sendo copiado:

`ditto -V {{caminho/para/origem}} {{caminho/para/destino}}`

- Copia um determinado arquivo ou diretório, mantendo as permissões do arquivo original:

`ditto -rsrc {{caminho/para/origem}} {{caminho/para/destino}}`
