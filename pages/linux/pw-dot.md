# pw-dot

> Create `.dot` files of the PipeWire graph.
> See also: `dot`, for rendering graph.
> More information: <https://docs.pipewire.org/page_man_pw-dot_1.html>.

- Generate a graph to `pw.dot` file:

`pw-dot`

- Read objects from `pw-dump` JSON file:

`pw-dot {{-j|--json}} {{path/to/file.json}}`

- Specify an [o]utput file, showing [a]ll object types:

`pw-dot --output {{path/to/file.dot}} {{-a|--all}}`

- Print `.dot` graph to `stdout`, showing all object properties:

`pw-dot --output - {{-d|--detail}}`

- Generate a graph from a [r]emote instance, showing only linked objects:

`pw-dot --remote {{remote_name}} {{-s|--smart}}`

- Lay the graph from [l]eft to [r]ight, instead of dot's default top to bottom:

`pw-dot {{-L|--lr}}`

- Lay the graph using 90-degree angles in edges:

`pw-dot {{-9|--90}}`

- Display help:

`pw-dot --help`
