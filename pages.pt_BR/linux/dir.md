# dir

> Lista o conteúdo do diretório usando uma linha por arquivo, caractéres especiais são representados por sequências de escape com barra invertida.
> Funciona como `ls -C --escape`.
> Mais informações: <https://manned.org/dir>.

- Listar todos os arquivos, incluindo arquivos ocultos:

`dir {{[-a|--all]}}`

- Listar arquivos exibindo o autor (`-l` é necessário):

`dir -l --author`

- Listar arquivos excluindo aqueles que correspondem a um padrão específico:

`dir --hide {{padrão}}`

- Listar subdiretórios recursivamente:

`dir {{[-R|--recursive]}}`

- Exibir ajuda:

`dir --help`
