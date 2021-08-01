# graphml2gv

> Convert a graph from the `graphml` format to the `gv` format.
> Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> More information: <http://graphviz.org/pdf/graphml2gv.1.pdf>.

- Convert a graph from the `gml` format to the `gv` format:

`graphml2gv -o output.gv input.gml`

- Make same conversion using `stdin` and `stdout`:

`cat input.gml | graphml2gv > output.gv`

- Display help:

`graphml2gv -?`
