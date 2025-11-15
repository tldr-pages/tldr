# mm2gv

> Convert a graph from Matrix Market `mm` format to `gv` format.
> Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> More information: <https://graphviz.org/pdf/mm2gv.1.pdf>.

- Convert a graph from `mm` to `gv` format:

`mm2gv -o {{output.gv}} {{input.mm}}`

- Convert a graph using `stdin` and `stdout`:

`cat {{input.mm}} | mm2gv > {{output.gv}}`

- Display help:

`mm2gv -?`
