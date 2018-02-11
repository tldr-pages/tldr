# zip

> Package and compress (archive) files into zip file.

- Package and compress a directory and its contents, [r]ecursively:

`zip -r {{compressed.zip}} {{/path/to/dir}}`

- E[x]clude unwanted files from being added to the compressed archive:

`zip -r {{compressed.zip}} {{path/to/dir}} -x {{path/to/exclude}}`

- Archive a directory and its contents with the highest level [9] of compression:

`zip -r -{{9}} {{compressed.zip}} {{/path/to/dir}}`

- Package and compress multiple directories and files:

`zip -r {{compressed.zip}} {{/path/to/dir1 /path/to/dir2 /path/to/file}}`

- Create an encrypted archive (user will be prompted for a password):

`zip -e -r {{compressed.zip}} {{path/to/dir}}`

- Add files to an existing zip file:

`zip {{compressed.zip}} {{path/to/file}}`

- Delete files from an existing zip file:

`zip -d {{compressed.zip}} "{{foo/*.tmp}}"`

- Archive a directory and its contents to a multi-part [s]plit zip file (e.g. 3GB parts):

`zip -r -s {{3g}} {{compressed.zip}} {{path/to/dir}}`
