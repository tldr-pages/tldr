# pacgraph

> Draw a graph of installed packages to PNG/SVG/GUI/console.
> More information: <https://github.com/keenerd/pacgraph>.

- Produce an SVG and PNG graph:

`pacgraph`

- Produce an SVG graph:

`pacgraph --svg`

- Print summary to console:

`pacgraph --console`

- Override the default filename/location (Note: Do not specify the file extension):

`pacgraph --file={{path/to/file}}`

- Change the color of packages that are not dependencies:

`pacgraph --top={{color}}`

- Change the color of package dependencies:

`pacgraph --dep={{color}}`

- Change the background color of a graph:

`pacgraph --background={{color}}`

- Change the color of links between packages:

`pacgraph --link={{color}}`
