# svgo

> SVG Optimizer: optimizing Scalable Vector Graphics files. Based in Node.js.
> It applies a series of transformation rules (plugins), which can be toggled individually.
> More information: <https://github.com/svg/svgo>.

- Optimize a file using the default plugins (overwrites the original file):

`svgo {{test.svg}}`

- Optimize a file and save the result to another file:

`svgo {{test.svg}} -o {{test.min.svg}}`

- Optimize all SVG files within a directory (overwrites the original files):

`svgo -f {{path/to/directory/with/svg/files}}`

- Optimize all SVG files within a directory and save the resulting files to another directory:

`svgo -f {{path/to/input/directory}} -o {{path/to/output/directory}}`

- Optimize SVG content passed from another command, and save the result to a file:

`{{cat test.svg}} | svgo -i - -o {{test.min.svg}}`

- Optimize a file and print out the result:

`svgo {{test.svg}} -o -`

- Show available plugins:

`svgo --show-plugins`
