# unzip

> Ferramenta de descompactação de arquivos zip.
> Mais informações: <https://manned.org/unzip>.

- Extrai arquivos zip:

`unzip {{caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...}}`

- Extrai arquivos zip para caminhos específicos:

`unzip {{caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...}} -d {{caminho/para}}`

- Lista conteúdos de arquivos zip:

`unzip -l {{caminho/para/arquivo.zip}}`

- Extrai arquivos zip sem a estrutura dos diretórios:

`unzip -j {{caminho/para/arquivo.zip}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`
