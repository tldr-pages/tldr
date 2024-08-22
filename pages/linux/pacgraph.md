# ls

> Draws a graph of installed packages to PNG/SVG/GUI/console. Good for finding bloat.
> More information: https://github.com/keenerd/pacgraph.

- Produce svg and png graph:

`pacgraph`

- Produce svg graph

`pacgraph --svg`

- Print summary to console:

`pacgraph --console`

- Override default filename/location. Do not specify extension:

`pacgraph --file=FILENAME`

- Change color of packages which are not dependencies:

`pacgraph --top=COLOR`

- Change color of package dependencies

`pacgraph --dep=COLOR`

- Change background color of a graph:

`pacgraph --background=COLOR`

- Change color of links between packages:

`pacgraph --link=COLOR`
