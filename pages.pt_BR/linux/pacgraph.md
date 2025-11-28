# pacgraph

> Desenha um grafo de pacotes instalados para PNG/SVG/GUI/console.
> Mais informações: <https://manned.org/pacgraph>.

- Produz um grafo em SVG e PNG:

`pacgraph`

- Produz um grafo SVG:

`pacgraph --svg`

- Imprime um resumo para o console:

`pacgraph --console`

- Substitui o nome de arquivo ou local padrão (Nota: não especifique a extensão do arquivo):

`pacgraph --file={{caminho/para/arquivo}}`

- Altera a cor dos pacotes que não são dependências:

`pacgraph --top={{cor}}`

- Altera a cor das dependências de pacotes:

`pacgraph --dep={{cor}}`

- Altera a cor de fundo de um grafo:

`pacgraph --background={{cor}}`

- Altera a cor dos links entre pacotes:

`pacgraph --link={{cor}}`
