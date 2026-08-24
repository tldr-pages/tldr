# pacgraph

> Draw a graph of installed packages to PNG/SVG/GUI/console.
> More information: <https://manned.org/pacgraph>.

- Produce an SVG and PNG graph:

`pacgraph`

- Produce an SVG graph:

`pacgraph {{[-s|--svg]}}`

- Print summary to console:

`pacgraph {{[-c|--console]}}`

- Override the default filename/location (Note: Do not specify the file extension):

`pacgraph {{[-f|--file]}} {{path/to/file}}`

- Change the color of packages that are not dependencies:

`pacgraph {{[-t|--top]}} {{color}}`

- Change the color of package dependencies:

`pacgraph {{[-d|--dep]}} {{color}}`

- Change the background color of a graph:

`pacgraph {{[-b|--background]}} {{color}}`

- Change the color of links between packages:

`pacgraph {{[-l|--link]}} {{color}}`
