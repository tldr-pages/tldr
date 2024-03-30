# fdp

> Renderiza uma imagem de um gráfico de rede `force-directed` a partir de um arquivo `graphviz`.
> Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
> Mais informações: <https://graphviz.org/doc/info/command.html>.

- Renderiza uma imagem PNG com um nome de arquivo baseado no nome do arquivo de entrada e formato de saída (-O maiúsculo):

`fdp -T png -O {{caminho/para/entrada.gv}}`

- Renderiza uma imagem SVG com o nome do arquivo de saída especificado (-o minúsculo):

`fdp -T svg -o {{caminho/para/imagem.svg}} {{caminho/para/entrada.gv}}`

- Renderiza a saída nos formatos:

`fdp -T {{ps|pdf|svg|fig|png|gif|jpg|json|dot}} -O {{caminho/para/entrada.gv}}`

- Renderiza uma imagem GIF usando `stdin` e `stdout`:

`echo "{{digraph {isso -> aquilo} }}" | fdp -T gif > {{caminho/para/imagem.gif}}`

- Exibe ajuda:

`fdp -?`
