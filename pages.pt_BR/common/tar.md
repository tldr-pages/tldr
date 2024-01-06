# tar

> Ferramenta de compressão de arquivos.
> Utilizado com metodos de compressão como o de gzip ou bzip2.
> Mais informações: <https://www.gnu.org/software/tar>.

- [C]ria um arquivo compactado e o escreve para um arquivo:

`tar cf {{caminho/para/alvo.tar}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`

- [C]ria um arquivo g[z]ip e o escreve para um arquivo:

`tar czf {{alvo.tar.gz}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`

- [C]ria um arquivo g[z]ip a partir de um diretório usando caminhos relativos:

`tar czf {{caminho/para/alvo.tar.xz}} --directory={{caminho/para/diretório}} .`

- E[x]trai arquivos de um arquivo (compactado):

`tar xvf {{origem.tar[.gz|.bz2|.xz]}}`

- E[x]trai um arquivo (compactado) para um diretório alvo:

`tar xf {{caminho/para/origem.tar[.gz|.bz2|.xz]}} --directory={{caminho/para/diretório}}`

- [C]ria um arquivo compactado e o escreve para um arquivo, usando a extensão de arquivo para determinar automaticamente a compressão do programa:

`tar caf {{caminho/para/alvo.tar.xz}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`

- Lista arquivos de um arquivo tar:

`tar tvf {{input.tar}}`

- Extrai arquivos que correspondam a um padrão de um arquivo compactado:

`tar xf {{caminho/para/alvo.tar}} --wildcards "{{*.html}}"`
