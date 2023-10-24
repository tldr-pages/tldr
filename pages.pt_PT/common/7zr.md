# 7z

> Compactador de arquivos com uma alta taxa de compressão.
> Semelhante ao '7z', com a diferença que suporta apenas ficheiros '.7z'.
> Mais informações: <https://manned.org/7zr>.

- Adicionar um ficheiro ou diretório a um novo ou existente arquivo:

`7z a {{diretório/arquivo_compactado.7z}} {{diretório/ficheiro_ou_diretório}}`

- Encripa um arquivo existente (incluindo filenames):

`7z a {{diretório/ficheiro_encriptado.7z}} -p{{palavra-passe}} -mhe=on {{diretório/arquivo_compactado.7z}}`

- Descompactar um arquivo mantendo a estrutura de diretórios original:

`7z x {{diretório/arquivo_compactado.7z}}`

- Descompactar um arquivo para um diretório especificado pelo utilizador:

`7z x {{diretório/arquivo_compactado.7z}} -o{{localização/do/directório}}`

- Descompactar um arquivo para a saída padrão (stdout):

`7z x {{diretório/arquivo_compactado.7z}} -so`

- Listar os conteúdos de um arquivo:

`7z l {{diretório/arquivo_compactado.7z}}`

- Listar todos os tipos de arquivamento/compressão disponíveis:

`7z i`
