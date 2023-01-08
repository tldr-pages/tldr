# gv2gxl

> Convert a graph from `gv` to `gxl` format.
> Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> More information: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- Convert a graph from `gv` to `gxl` format:

`gv2gxl -o {{output.gxl}} {{input.gv}}`

- Convert a graph using `stdin` and `stdout`:

`cat {{input.gv}} | gv2gxl > {{output.gxl}}`

- Display help:

`gv2gxl -?`
