# zip

> Ferramenta de compressão de arquivos em arquivos zip.
> Mais informações: <https://manned.org/zip>.

- Compacta arquivos:

`zip {{compactado.zip}} {{arquivo1}} {{arquivo2}} {{arquivo3}}`

- Compacta arquivos e diretórios recursivamente:

`zip --recurse-paths {{compactado.zip}} {{arquivo}} {{caminho/do/diretorio1}} {{caminho/do/diretorio2}}`

- Compacta um diretório usando o nível de compressão máximo [9]:

`zip --{{9}} --recurse-paths {{compactado.zip}} {{caminho/do/diretorio}}`

- Cria um arquivo compactado criptografado (o usuário deverá inserir uma senha):

`zip --encrypt --recurse-paths {{compactado.zip}} {{caminho/do/diretorio}}`

- Compacta arquivos de um diretório excluindo arquivos específicos:

`zip --exclude {{caminho/a/ser/excluido}} --recurse-paths {{compactado.zip}} {{caminho/do/diretorio}}`

- Adiciona arquivos a um arquivo zip existente:

`zip {{arquivo_existente.zip}} {{arquivo}}`

- Remove arquivo dentro de um arquivo zip existente:

`zip --delete {{arquivo_existente.zip}} "{{arquivo}}"`

- Lista arquivos dentro de um zip sem extraí-los:

`zip --show-files {{arquivo.zip}}`
