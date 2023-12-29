# zip

> Ferramenta de compressão de arquivos em arquivos zip.
> Mais informações: <https://manned.org/zip>.

- Compacta arquivos em um arquivo zip:

`zip {{output.zip}} {{arquivo1}} {{arquivo2}} {{arquivo3}}`

- Compacta todos os arquivos de um diretório:

`zip {{output.zip}} {{caminho/do/diretorio/*}}`

- Adiciona arquivos a um arquivo zip existente:

`zip {{arquivo_existente.zip}} {{caminho/do/diretorio}}`

- Compacta todos os arquivos de um diretório mantendo estruturas de diretórios:

`zip -r {{output.zip}} {{caminho/do/diretorio}}`

- Compacta arquivos de um diretório excluindo arquivos específicos:

`zip -r {{output.zip}} {{caminho/do/diretorio}} -x {{caminho/a/ser/excluido}}`

- Compacta arquivos definindo o nível de compressão [9]:

`zip -r -{{9}} {{output.zip}} {{caminho/do/diretorio}}`

- Deleta arquivos de um arquivo zip:

`zip -d {{output.zip}} "{{foo/*.ext}}"`
