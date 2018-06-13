# expand

> Uncompress one or more Windows Cabinet files.

- Uncompress a single-file Cabinet file to the specified directory:

`expand {{path/to/file.cab}} {{path/to/directory}}`

- Display a list of files in the source Cabinet file:

`expand {{path/to/file.cab}} {{path/to/directory}} -d`

- Uncompress all files from the Cabinet file:

`expand {{path/to/file.cab}} {{path/to/directory}} -f:*`

- Uncompress a specific file from a Cabinet file:

`expand {{path/to/file.cab}} {{path/to/directory}} -f:{{file}}`

- Ignore the directory structure when uncompressing:

`expand {{path/to/file.cab}} {{path/to/directory}} -i`
