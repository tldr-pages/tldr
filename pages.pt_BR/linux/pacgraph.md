# pacgraph

> Desenha um grafo de pacotes instalados para PNG/SVG/GUI/console.
> Mais informações: <https://manned.org/pacgraph>.

- Produz um grafo em SVG e PNG:

`pacgraph`

- Produz um grafo SVG:

`pacgraph {{[-s|--svg]}}`

- Imprime um resumo para o console:

`pacgraph {{[-c|--console]}}`

- Substitui o nome de arquivo ou local padrão (Nota: não especifique a extensão do arquivo):

`pacgraph {{[-f|--file]}} {{caminho/para/arquivo}}`

- Altera a cor dos pacotes que não são dependências:

`pacgraph {{[-t|--top]}} {{cor}}`

- Altera a cor das dependências de pacotes:

`pacgraph {{[-d|--dep]}} {{cor}}`

- Altera a cor de fundo de um grafo:

`pacgraph {{[-b|--background]}} {{cor}}`

- Altera a cor dos links entre pacotes:

`pacgraph {{[-l|--link]}} {{cor}}`
