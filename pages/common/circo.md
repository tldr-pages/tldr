# circo

> Render an image of a `circular` network graph from a `graphviz` file.
> Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
> More information: <https://graphviz.org/doc/info/command.html>.

- Render a PNG image with a filename based on the input filename and output format (uppercase -O):

`circo -T {{png}} -O {{path/to/input.gv}}`

- Render a SVG image with the specified output filename (lowercase -o):

`circo -T {{svg}} -o {{path/to/image.svg}} {{path/to/input.gv}}`

- Render the output in PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, or DOT format:

`circo -T {{format}} -O {{path/to/input.gv}}`

- Render a GIF image using `stdin` and `stdout`:

`echo "{{digraph {this -> that} }}" | circo -T {{gif}} > {{path/to/image.gif}}`

- Display help:

`circo -?`
