# neato

> Render an image of a `linear undirected` network graph from a `graphviz` file.
> Layouts are `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
> More information: <http://graphviz.org/doc/info/command.html>.

- Render a `png` image with a filename based on the input filename and output format:

`neato -Tpng -O {{path/to/input.gv}}`

- Render a `svg` image with the specified output filename:

`neato -Tsvg -o {{path/to/image.svg}} {{path/to/input.gv}}`

- Render the output in `ps`, `pdf`, `svg`, `fig`, `png`, `gif`, `jpg`, `json`, or `dot` format:

`neato -T{{format}} -O {{path/to/input.gv}}`

- Render a `gif` image using `stdin` and `stdout`:

`echo "{{graph {this -- that} }}" | neato -Tgif > {{path/to/image.gif}}`

- Display help:

`neato -?`
