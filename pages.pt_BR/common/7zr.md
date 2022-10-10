# 7zr

> Um compactador de arquivos com alta taxa de compressão.
> Versão do `7z` com suporte apenas para o formato `.7z`.
> Mais informações: <https://www.7-zip.org>.

- Compactar um arquivo ou diretório:

`7zr a {{arquivo_compactado.7z}} {{caminho/arquivo_ou_diretorio}}`

- Criptografa um arquivo existente (incluindo cabeçalhos):

`7zr a {{arquivo_criptografado.7z}} -p{{senha}} -mhe=on {{arquivo.7z}}`

- Descompacta um arquivo mantendo a estrutura de diretórios original:

`7zr x {{arquivo_compactado.7z}}`

- Descompacta um arquivo em um diretório específicado pelo usuário:

`7zr x {{arquivo.7z}} -o{{caminho/diretório}}`

- Descompactar um arquivo para a saída padrão:

`7zr x {{path/to/archive.7z}} -so`

- Exibe o conteúdo de um arquivo:

`7zr l {{arquivo.7z}}`

- Exibe os tipos de arquivamento/compressão disponíveis:

`7zr i`
