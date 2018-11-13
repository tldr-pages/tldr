# svgo

> SVG Optimizer: a Nodejs-based tool for optimizing Scalable Vector Graphics files.
> It applies a series of transformation rules (plugins), which can be toggled individually.

- Optimize a file using the default plugins (overwrites the original file):

`svgo {{test.svg}}`

- Optimize a file and save the result to another file:

`svgo {{test.svg}} {{test.min.svg}}`

- Optimize all SVG files within a folder (overwrites the original files):

`svgo -f {{path/to/folder/with/svg/files}}`

- Optimize all SVG files within a folder and save the resulting files to another folder:

`svgo -f {{path/to/input/folder}} -o {{path/to/output/folder}}`

- Optimize SVG content passed from another command, and save the result to a file:

`{{cat test.svg}} | svgo -i - -o {{test.min.svg}}`

- Optimize a file and print out the result:

`svgo {{test.svg}} -o -`

- Optimize a file making sure a given plugin is enabled:

`svgo --enable={{plugin_name}}`

- Show available plugins:

`svgo --show-plugins`
