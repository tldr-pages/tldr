# unzip

> Ferramenta de descompactação de arquivos zip.
> Mais informações: <https://manned.org/unzip>.

- Extrai arquivos zip:

`unzip {{caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...}}`

- Extrai arquivos zip para caminhos específicos:

`unzip {{caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...}} -d {{caminho/para/saída}}`

- Extrai arquivos/diretórios de arquivos para `stdout`:

`unzip -c {{caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...}}`

- Extrai o conteúdo do(s) arquivo(s) para `stdout` ao lado dos nomes dos arquivos extraídos:

`unzip -O {{gbk}} {{caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...}}`

- Lista conteúdos de arquivos zip:

`unzip -l {{caminho/para/arquivo.zip}}`

- Extrai arquivos zip sem a estrutura dos diretórios:

`unzip -j {{caminho/para/arquivo.zip}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`
