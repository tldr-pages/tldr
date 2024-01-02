# tar

> Ferramenta de compressão de arquivos.
> Utilizado com metodos de compressão como o de gzip ou bzip2.
> Mais informações: <https://www.gnu.org/software/tar>.

- Compacta arquivos em um arquivo tar:

`tar -cvf {{output.tar}} {{arquivo1}} {{arquivo2}} {{arquivo3}}`

- Compacta arquivos em arquivo gzip:

`tar -czvf {{output.tar.gz}} {{arquivo1}} {{arquivo2}} {{arquivo3}}`

- Compacta arquivos definindo tipo de compressão automaticamente por extensão:

`tar -cavf {{output.tar.xz}} {{arquivo1}} {{arquivo2}} {{arquivo3}}`

- Extrai arquivos de um arquivo compactado:

`tar -xvf {{input.tar[.gz|.bz2|.xz]}}`

- Extrai arquivos de um arquivo compactado filtrando por gzip:

`tar -xzvf {{input.tar[.gz|.bz2|.xz]}}`

- Extrai arquivos de um arquivo compactado para um diretório específico:

`tar -xvf {{input.tar[.gz|.bz2|.xz]}} -C {{diretório}}`

- Extrai arquivos seguindo um padrão:

`tar -xvf {{input.tar}} --wildcards "{{*.html}}"`

- Lista arquivos de um arquivo tar:

`tar -tvf {{input.tar}}`
