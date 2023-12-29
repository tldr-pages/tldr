# pw-dot

> Create `.dot` files of the PipeWire graph.
> See also: `dot` for rendering graph.
> More information: <https://docs.pipewire.org/page_man_pw-dot_1.html>.

- Generate a graph to `pw.dot` file:

`pw-dot`

- Specify a filename showing all object types:

`pw-dot --all --output {{path/to/file.dot}}`

- Print `.dot` graph to stdout showing all object properties:

`pw-dot --detail --output -`

- Generate a graph from a remote instance showing only linked objects:

`pw-dot --smart --remote {{remote_name}}`

- Lay the graph from left to right, instead of dot's default top to bottom:

`pw-dot --lr`

- Lay the graph using 90-degree angles in edges:

`pw-dot --90`
