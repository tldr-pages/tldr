# svgo

> SVG Optimizer: a Nodejs-based tool for optimizing SVG vector graphics files.
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

- Optimize SVG content passed as a string, and save the result to a file:

`svgo -s '{{<svg version="1.1">test</svg>}}' -o {{test.min.svg}}`

- Optimize SVG content passed as a base64 Data URI, and print out the result:

`svgo -s '{{data:image/svg+xml;base64,…}}' -o -`

- Optimize and compress a file from .svg to .svgz:

`svgo test.svg -o - | gzip -cfq9 > test.svgz`

- Optimize a file making sure a given plugin is enabled:

`svgo --enable={{plugin_name}}`

- Optimize a file using a custom configuration file, to extend or replace the default one (`.svgo.yml`):

`svgo --config={{myconfig.yml}} test.svg`

- Optimize a file with all plugins disabled except a specific one:

`echo "plugins:" > c && svgo --config=c --enable={{plugin_name}} test.svg`

- Show available plugins:

`svgo --show-plugins`
