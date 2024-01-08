# zip

> Ferramenta de compressão de arquivos em arquivos zip.
> Mais informações: <https://manned.org/zip>.

- Adiciona arquivos/diretórios a um arquivo zip específico ([r]ecusivamente):

`zip -r {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Remove arquivos de um arquivo zip ([d]eleta):

`zip -d {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Compacta arquivos/diretórios e[x]cluindo arquivos específicos:

`zip -r {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}} -x {{caminho/a/ser/excluido}}`

- Compacta arquivos com um nível de compressão específico (0 - o mais baixo, 9 - o mais alto):

`zip -r -{{0-9}} {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Cria um zip encriptado com uma senha específica:

`zip -r -e {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Compacta arquivos/diretórios para um zip dividido em múltiplas partes (p. ex. partes de 3 GB):

`zip -r -s {{3g}} {{caminho/para/comprimido.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Print a specific archive contents:

`zip -sf {{caminho/para/comprimido.zip}}`
