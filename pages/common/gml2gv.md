# gml2gv

> Convert a graph from `gml` to `gv` format.
> Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> More information: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- Convert a graph from `gml` to `gv` format:

`gml2gv -o {{output.gv}} {{input.gml}}`

- Convert a graph using stdin and stdout:

`cat {{input.gml}} | gml2gv > {{output.gv}}`

- Display help:

`gml2gv -?`
