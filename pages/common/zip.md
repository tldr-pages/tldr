# zip

> Package and compress (archive) files into zip file.
> More information: <https://manned.org/zip>.

- Package and compress files:

`zip {{compressed.zip}} {{path/to/file_1}} {{path/to/file_2}}`

- Package and compress files and directories recursively:

`zip --recurse-paths {{compressed.zip}} {{path/to/file}} {{path/to/directory_1}} {{path/to/directory_2}}`

- Archive a directory and its contents with the highest level [9] of compression:

`zip -{{9}} --recurse-paths {{compressed.zip}} {{path/to/directory}}`

- Create an encrypted archive (user will be prompted for a password):

`zip --encrypt --recurse-paths {{compressed.zip}} {{path/to/directory}}`

- Exclude unwanted files from being added to the compressed archive:

`zip --exclude {{path/to/exclude}} --recurse-paths {{compressed.zip}} {{path/to/directory}}`

- Add files to an existing zip file:

`zip {{compressed.zip}} {{path/to/file}}`

- Delete entries from an existing zip file:

`zip --delete {{compressed.zip}} "{{foo/file}}" "{{foo/bar/*}}" "{{*.ext}}"`

- List files within a specified archive (without extracting them):

`zip --show-files {{compressed.zip}}`
