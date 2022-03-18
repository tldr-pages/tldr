# expand

> Uncompress one or more Windows Cabinet files. Wildcards are supported.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/expand>.

- Uncompress the single-file Cabinet file to the specified directory:

`expand {{path/to/file.cab}} {{path/to/directory}}`

- Print all files in the specified Cabinet file:

`expand {{path/to/file.cab}} {{path/to/directory}} -d`

- Uncompress all files from the Cabinet file:

`expand {{path/to/file.cab}} {{path/to/directory}} -f:*`

- Uncompress the specified file from the Cabinet file:

`expand {{path/to/file.cab}} {{path/to/directory}} -f:{{path/to/file}}`

- Ignore the directory structure when uncompressing, and add them to the single directory:

`expand {{path/to/file.cab}} {{path/to/directory}} -i`
