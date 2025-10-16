# graphviz

> A collection of tools for creating and manipulating graph visualizations.
> More information: <https://graphviz.org>.

- Render a graph using the dot layout engine to a specific format:

`dot -T{{format}} {{path/to/input.gv}} -o {{path/to/output}}`

- Render a graph using a specific layout engine:

`{{neato|dot|circo|fdp|osage|sfdp|twopi}} -T{{format}} {{path/to/input.gv}} -o {{path/to/output}}`

- Render a graph to an SVG file:

`dot -Tsvg {{path/to/input.gv}} -o {{path/to/output.svg}}`

- Render a graph to a PNG file:

`dot -Tpng {{path/to/input.gv}} -o {{path/to/output.png}}`

- Render a graph to a PDF file:

`dot -Tpdf {{path/to/input.gv}} -o {{path/to/output.pdf}}`

- Display available output formats:

`dot -T?`

- Display version information:

`dot -V`
