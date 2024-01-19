# 7za

> Um compactador de arquivos com alta taxa de compressão.
> Versão compacta do `7z`, com suporte para menos tipos de arquivamento/compressão.
> Mais informações: <https://manned.org/7za>.

- Compacta um arquivo ou diretório:

`7za a {{caminho/para/arquivo_compactado.7z}} {{caminho/para/arquivo_ou_diretório}}`

- Criptografa um arquivo existente (incluindo cabeçalhos):

`7za a {{caminho/para/arquivo_criptografado.7z}} -p{{senha}} -mhe {{on}} {{caminho/para/arquivo_compactado.7z}}`

- Descompacta um arquivo mantendo a estrutura de diretórios original:

`7za x {{caminho/para/arquivo_compactado.7z}}`

- Descompacta um arquivo em um diretório específicado pelo usuário:

`7za x {{caminho/para/arquivo_compactado.7z}} -o{{caminho/para/diretório}}`

- Descompacta um arquivo para a saída padrão:

`7za x {{caminho/para/arquivo_compactado.7z}} -so`

- Compacta utilizando um tipo específico de arquivamento/compressão:

`7za a -t{{zip|gzip|bzip2|tar}} {{caminho/para/arquivo_compactado.7z}} {{caminho/para/arquivo_ou_diretório}}`

- Exibe o conteúdo de um arquivo:

`7za l {{caminho/para/arquivo_compactado.7z}}`

- Define o nível de compressão (maior significa mais compressão, porém mais lento):

`7za a {{caminho/para/arquivo_compactado.7z}} -mx={{0|1|3|5|7|9}} {{caminho/para/arquivo_ou_diretório}}`
