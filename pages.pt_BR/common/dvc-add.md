# dvc add

> Adiciona um arquivo modificado para o índice.
> Mais informações: <https://dvc.org/doc/command-reference/add>.

- Adiciona um arquivo para o índice:

`dvc add {{caminho/para/arquivo}}`

- Adiciona um diretório para o índice:

`dvc add {{caminho/para/diretorio}}`

- Adiciona recursivamente todos os arquivos em um dado diretório:

`dvc add --recursive {{caminho/para/diretorio}}`

- Adiciona um arquivo com o nome `.dvc` customizado:

`dvc add --file {{nome_customizado.dvc}} {{caminho/para/arquivo}}`
