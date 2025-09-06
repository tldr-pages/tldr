# svgr

> Transform SVGs into React components.
> More information: <https://react-svgr.com>.

- Transform a SVG file into a React component to `stdout`:

`svgr -- {{path/to/file.svg}}`

- Transform a SVG file into a React component using TypeScript to `stdout`:

`svgr --typescript -- {{path/to/file.svg}}`

- Transform a SVG file into a React component using JSX transform to `stdout`:

`svgr --jsx-runtime automatic -- {{path/to/file.svg}}`

- Transform all SVG files from a directory to React components into a specific directory:

`svgr --out-dir {{path/to/output_directory}} {{path/to/input_directory}}`

- Transform all SVG files from a directory to React components into a specific directory skipping already transformed files:

`svgr --out-dir {{path/to/output_directory}} --ignore-existing {{path/to/input_directory}}`

- Transform all SVG files from a directory to React components into a specific directory using a specific case for filenames:

`svgr --out-dir {{path/to/output_directory}} --filename-case {{camel|kebab|pascal}} {{path/to/input_directory}}`

- Transform all SVG files from a directory to React components into a specific directory without generating an index file:

`svgr --out-dir {{path/to/output_directory}} --no-index {{path/to/input_directory}}`
