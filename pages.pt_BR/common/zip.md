# zip

> Ferramenta de compressão de arquivos em arquivos zip.
> Mais informações: <https://manned.org/zip>.

- Compacta todos os arquivos de um diretório mantendo estruturas de diretórios:

`zip -r {{caminho/para/output.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Deleta arquivos de um arquivo zip:

`zip -d {{caminho/para/output.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`

- Compacta arquivos de um diretório excluindo arquivos específicos:

`zip -r {{caminho/para/output.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}} -x {{caminho/a/ser/excluido}}`

- Compacta arquivos definindo o nível de compressão [9]:

`zip -r -{{0-9}} {{caminho/para/output.zip}} {{caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...}}`
