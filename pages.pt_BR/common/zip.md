# zip

> Ferramenta de compressão de arquivos em arquivos zip.
> Mais informações: <https://manned.org/zip>.

- Adiciona arquivos/diretórios a um arquivo zip específico ([r]ecusivamente):

`zip {{[-r|--recurse-paths]}} {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Remove arquivos de um arquivo zip ([d]eleta):

`zip {{[-d|--delete]}} {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Compacta arquivos/diretórios e[x]cluindo arquivos específicos:

`zip {{[-r|--recurse-paths]}} {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}} {{[-x|--exclude]}} {{caminho/a/ser/excluido}}`

- Compacta arquivos com um nível de compressão específico (0 - o mais baixo, 9 - o mais alto):

`zip {{[-r|--recurse-paths]}} -{{0-9}} {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Cria um zip encriptado com uma senha específica:

`zip {{[-re|--recurse-paths --encrypt]}} {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Compacta arquivos/diretórios para um zip dividido em múltiplas partes (p. ex. partes de 3 GB):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Print a specific archive contents:

`zip {{[-sf|--split-size --freshen]}} {{caminho/para/comprimido.zip}}`
