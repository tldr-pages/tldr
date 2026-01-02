# svgo

> SVG Optimizer: optimizing Scalable Vector Graphics files. Based in Node.js.
> It applies a series of transformation rules (plugins), which can be toggled individually.
> More information: <https://manned.org/svgo>.

- Optimize a file using the default plugins (overwrites the original file):

`svgo {{test.svg}}`

- Optimize a file and save the result to another file:

`svgo {{test.svg}} {{[-o|--output]}} {{test.min.svg}}`

- Optimize all SVG files within a directory (overwrites the original files):

`svgo {{[-f|--folder]}} {{path/to/directory_with_svg_files}}`

- Optimize all SVG files within a directory and save the resulting files to another directory:

`svgo {{[-f|--folder]}} {{path/to/input_directory}} {{[-o|--output]}} {{path/to/output_directory}}`

- Optimize SVG content passed from another command, and save the result to a file:

`{{cat test.svg}} | svgo {{[-i|--input]}} - {{[-o|--output]}} {{test.min.svg}}`

- Optimize a file and print out the result:

`svgo {{test.svg}} {{[-o|--output]}} -`

- Show available plugins:

`svgo --show-plugins`
