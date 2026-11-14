# gxl2dot

> Convert a graph from `gxl` to `dot` format.
> Converter paired with `dot2gxl`.
> More information: <https://web.mit.edu/spin_v4.2.5/share/graphviz/doc/pdf/gxl2dot.pdf>.

- Convert a graph from `gxl` to `dot` format:

`gxl2dot -o {{output.dot}} {{input.gxl}}`

- Convert a graph using `stdin` and `stdout`:

`cat {{input.gxl}} | gxl2dot > {{output.dot}}`

- Force the input to be treated as GXL and generate DOT output:

`gxl2dot -d -o {{output.dot}} {{input_file}}`

- Display help:

`gxl2dot -?`
