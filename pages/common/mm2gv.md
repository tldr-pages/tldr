# mm2gv

> Convert a graph from the Matrix Market `mm` format to the `gv` format.
> Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> More information: <http://graphviz.org/pdf/mm2gv.1.pdf>.

- Convert a graph from the `mm` format to the `gv` format:

`mm2gv -o output.gv input.mm`

- Make same conversion using `stdin` and `stdout`:

`cat input.mm | mm2gv > output.gv`

- Display help:

`mm2gv -?`
