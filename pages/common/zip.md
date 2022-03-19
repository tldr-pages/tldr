# zip

> Package and compress (archive) files into zip file.
> More information: <https://manned.org/zip>.

- Package and compress files:

`zip {{path/to/compressed.zip}} {{path/to/file1 path/to/file2 ...}}`

- Package and compress files and directories recursively:

`zip --recurse-paths {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Archive a directory and its contents with the highest level [9] of compression:

`zip -{{9}} --recurse-paths {{path/to/compressed.zip}} {{path/to/directory}}`

- Create an encrypted archive (user will be prompted for a password):

`zip --encrypt --recurse-paths {{path/to/compressed.zip}} {{path/to/directory}}`

- Exclude unwanted files from being added to the compressed archive:

`zip --exclude {{path/to/exclude}} --recurse-paths {{compressed.zip}} {{path/to/directory}}`

- Add files to an existing zip file:

`zip {{path/to/compressed.zip}} {{path/to/file1 path/to/file2 ...}}`

- Delete entries from an existing zip file:

`zip --delete {{path/to/compressed.zip}} {{path/to/file_to_remove1 path/to/file_to_remove2 ...}}`

- List files within a specified archive (without extracting them):

`zip --show-files {{path/to/compressed.zip}}`
