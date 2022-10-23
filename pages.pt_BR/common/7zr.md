# 7zr

> Um compactador de arquivos com alta taxa de compressão.
> Versão do `7z` com suporte apenas para o formato `.7z`.
> Mais informações: <https://www.7-zip.org>.

- Compactar um arquivo ou diretório:

`7zr a {{caminho/para/arquivo_compactado.7z}} {{caminho/para/arquivo_ou_diretorio}}`

- Criptografa um arquivo existente (incluindo cabeçalhos):

`7zr a {{arquivo_criptografado.7z}} -p{{senha}} -mhe=on {{caminho/para/arquivo_compactado.7z}}`

- Descompacta um arquivo mantendo a estrutura de diretórios original:

`7zr x {{arquivo_compactado.7z}}`

- Descompacta um arquivo em um diretório específicado pelo usuário:

`7zr x {{caminho/para/arquivo_compactado.7z}} -o{{caminho/para/diretório}}`

- Descompacta um arquivo para a saída padrão:

`7zr x {{caminho/para/arquivo_compactado.7z}} -so`

- Exibe o conteúdo de um arquivo:

`7zr l {{caminho/para/arquivo_compactado.7z}}`

- Exibe os tipos de arquivamento/compressão disponíveis:

`7zr i`
