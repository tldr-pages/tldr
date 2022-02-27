# zip

> Ferramenta de compressão de arquivos em arquivos zip.
> Mais informações: <https://manned.org/zip>.

- Compacta arquivos:

`zip {{compactado.zip}} {{arquivo1}} {{arquivo2}} {{arquivo3}}`

- Compactar arquivos e diretórios [r]ecursivamente:

`zip -r {{compactado.zip}} {{arquivo}} {{caminho/do/diretorio1}} {{caminho/do/diretorio2}}`

- Compactar arquivos usando o nível de compressão máximo [9]:

`zip -r -{{9}} {{compactado.zip}} {{caminho/do/diretorio}}`

- Compactar arquivos de um diretório excluindo arquivos específicos:

`zip -r {{compactado.zip}} {{caminho/do/diretorio}} -x {{caminho/a/ser/excluido}}`

- Adicionar arquivos a um arquivo zip existente:

`zip {{arquivo_existente.zip}} {{arquivo}}`

- Remover arquivo dentro de um arquivo zip existente:

`zip -d {{arquivo_existente.zip}} "{{arquivo}}"`

- Listar arquivos dentro de um zip sem extraí-los:

`zip -sf {{arquivo.zip}}`
