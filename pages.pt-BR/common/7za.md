# 7za

> Um compactador de arquivos com alta taxa de compressão.
> Versão do `7z` com suporte para poucos tipos de arquivamento/compressão.
> Página oficial: <https://www.7-zip.org/>.

- Compactar um arquivo ou diretório:

`7za a {{arquivo_compactado.7z}} {{caminho/arquivo_ou_diretorio}}`

- Descompactar um arquivo mantendo a estrutura de diretórios original:

`7za x {{arquivo_compactado.7z}}`

- Compactar utilizando um tipo específico de arquivamento/compressão:

`7za a -t{{zip|gzip|bzip2|tar}} {{arquivo_compactado.7z}} {{caminho/arquivo_ou_diretorio}}`

- Exibir os tipos de arquivamento/compressão disponíveis:

`7za i`

- Exibir o conteúdo de um arquivo:

`7za l {{arquivo.7z}}`
