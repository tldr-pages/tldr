# 7za

> Compactador de arquivos com uma alta taxa de compressão.
> Semelhante to '7z', a principal diferença é que este suporta menos tipos de arquivamento/compressão.
> Mais informações: <https://manned.org/7za>.

- Compactar um ficheiro ou diretório:

`7za a {{diretório/arquivo_compactado.7z}} {{diretório/ficheiro_ou_diretório}}`

- Encriptar um arquivo existente (incluindo os nomes dos ficheiros):

`7za a {{diretório/ficheiro_encriptado.7z}} -p{{palavra-passe}} -mhe={{on}} {{diretório/arquivo_compactado.7z}}`

- Descompactar um arquivo mantendo a estrutura de diretórios original:

`7za x {{diretório/arquivo_compactado.7z}}`

- Descompactar um arquivo para uma diretório especificado pelo utilizador:

`7za x {{diretório/arquivo_compactado.7z}} -o{{localização/do/diretório}}`

- Descompactar um arquivo para a saída padrão (stdout):

`7za x {{diretório/arquivo_compactado.7z}} -so`

- Compactar utilizando um tipo específico de arquivamento/compressão:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{diretório/arquivo_compactado.7z}} {{diretório/ficheiro_ou_diretório}}`

- Listar os conteúdos de um arquivo:

`7za l {{diretório/arquivo_compactado.7z}}`

- Listar todos os tipos de arquivamento/compressão disponíveis:

`7za i`
