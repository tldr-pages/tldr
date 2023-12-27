# 7zr

> Compactador de arquivos com uma alta taxa de compressão.
> Semelhante ao '7z', com a diferença que suporta apenas ficheiros '.7z'.
> Mais informações: <https://manned.org/7zr>.

- Adiciona um ficheiro ou diretório a um novo ou existente arquivo:

`7zr a {{caminho/para/arquivo_compactado.7z}} {{caminho/para/ficheiro_ou_diretório}}`

- Encripa um arquivo existente (incluindo filenames):

`7zr a {{caminho/para/ficheiro_encriptado.7z}} -p{{palavra-passe}} -mhe=on {{caminho/para/arquivo_compactado.7z}}`

- Descompacta um arquivo mantendo a estrutura de diretórios original:

`7zr x {{caminho/para/arquivo_compactado.7z}}`

- Descompacta um arquivo para um diretório especificado pelo utilizador:

`7zr x {{caminho/para/arquivo_compactado.7z}} -o{{caminho/para/diretório}}`

- Descompacta um arquivo para a saída padrão (stdout):

`7zr x {{caminho/para/arquivo_compactado.7z}} -so`

- Lista os conteúdos de um arquivo:

`7zr l {{caminho/para/arquivo_compactado.7z}}`
