# 7za

> Um compactador de arquivos com alta taxa de compressão.
> Versão compacta do `7z`, com suporte para menos tipos de arquivamento/compressão.
> Mais informações: <https://www.7-zip.org>.

- Compactar um arquivo ou diretório:

`7za a {{arquivo_compactado.7z}} {{caminho/arquivo_ou_diretório}}`

- Criptografar um arquivo existente (incluindo cabeçalhos):

`7za a {{arquivo_criptografado.7z}} -p{{senha}} -mhe=on {{arquivo.7z}}`

- Descompactar um arquivo mantendo a estrutura de diretórios original:

`7za x {{arquivo_compactado.7z}}`

- Descompactar um arquivo em um diretório específicado pelo usuário:

`7za x {{arquivo.7z}} -o{{caminho/diretório}}`

- Descompactar um arquivo para a saída padrão:

`7za x {{path/to/archive.7z}} -so`

- Compactar utilizando um tipo específico de arquivamento/compressão:

`7za a -t{{zip|gzip|bzip2|tar}} {{caminho/para/arquivo.7z}} {{caminho/arquivo_ou_diretório}}`

- Exibir o conteúdo de um arquivo:

`7za l {{caminho/para/arquivo.7z}}`

- Exibir os tipos de arquivamento/compressão disponíveis:

`7za i`
