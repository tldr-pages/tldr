# gv2gml

> Convert a graph from `gv` to `gml` format.
> Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> More information: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- Convert a graph from `gv` to `gml` format:

`gv2gml -o {{output.gml}} {{input.gv}}`

- Convert a graph using stdin and stdout:

`cat {{input.gv}} | gv2gml > {{output.gml}}`

- Display help:

`gv2gml -?`
