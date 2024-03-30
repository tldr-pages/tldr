# 7za

> Compactador de arquivos com uma alta taxa de compressão.
> Semelhante to '7z', a principal diferença é que este suporta menos tipos de arquivamento/compressão.
> Mais informações: <https://manned.org/7za>.

- Compacta um ficheiro ou diretório:

`7za a {{caminho/para/ficheiro_compactado.7z}} {{caminho/para/ficheiro_ou_diretório}}`

- Encripta um arquivo existente (incluindo os nomes dos ficheiros):

`7za a {{caminho/para/ficheiro_encriptado.7z}} -p{{palavra-passe}} -mhe={{on}} {{caminho/para/ficheiro_compactado.7z}}`

- Descompacta um arquivo mantendo a estrutura de diretórios original:

`7za x {{caminho/para/ficheiro_compactado.7z}}`

- Descompacta um arquivo para uma diretório especificado pelo utilizador:

`7za x {{caminho/para/ficheiro_compactado.7z}} -o{{caminho/para/diretório}}`

- Descompacta um arquivo para a saída padrão (stdout):

`7za x {{caminho/para/ficheiro_compactado.7z}} -so`

- Compacta utilizando um tipo específico de arquivamento/compressão:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{caminho/para/ficheiro_compactado.7z}} {{caminho/para/ficheiro_ou_diretório}}`

- Lista os conteúdos de um arquivo:

`7za l {{caminho/para/ficheiro_compactado.7z}}`
