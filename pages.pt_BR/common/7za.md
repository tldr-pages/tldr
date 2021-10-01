# 7za

> Um compactador de arquivos com alta taxa de compressão.
> Versão compacta do `7z`, com suporte para menos tipos de arquivamento/compressão.
> Mais informações: <https://www.7-zip.org>.

- Compactar um arquivo ou diretório:

`7za a {{arquivo_compactado.7z}} {{caminho/arquivo_ou_diretório}}`

- Descompactar um arquivo mantendo a estrutura de diretórios original:

`7za x {{arquivo_compactado.7z}}`

- Compactar utilizando um tipo específico de arquivamento/compressão:

`7za a -t{{zip|gzip|bzip2|tar}} {{arquivo_compactado.7z}} {{caminho/arquivo_ou_diretório}}`

- Exibir os tipos de arquivamento/compressão disponíveis:

`7za i`

- Exibir o conteúdo de um arquivo:

`7za l {{arquivo.7z}}`
