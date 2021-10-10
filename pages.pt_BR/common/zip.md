# zip

> Ferramenta de compressão de arquivos em arquivos zip.
> Mais informações: <https://manned.org/zip>.

- Compactando arquivos em um arquivo zip:

`zip {{output.zip}} {{arquivo1}} {{arquivo2}} {{arquivo3}}`

- Compactando todos os arquivos de um diretório:

`zip {{output.zip}} {{caminho/do/diretorio/*}}`

- Adicionando arquivos a um arquivo zip existente:

`zip {{arquivo_existente.zip}} {{caminho/do/diretorio}}`

- Compactando todos os arquivos de um diretório mantendo estruturas de diretórios:

`zip -r {{output.zip}} {{caminho/do/diretorio}}`

- Compactando arquivos de um diretório excluindo arquivos específicos:

`zip -r {{output.zip}} {{caminho/do/diretorio}} -x {{caminho/a/ser/excluido}}`

- Compactando arquivos definindo o nível de compressão [9]:

`zip -r -{{9}} {{output.zip}} {{caminho/do/diretorio}}`

- Deletando arquivos de um arquivo zip:

`zip -d {{output.zip}} "{{foo/*.ext}}"`
