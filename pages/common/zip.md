# zip

> Package and compress (archive) files into zip file.

- Package and compress a directory and its contents, [r]ecursively:

`zip -r {{compressed.zip}} {{/path/to/dir}}`

- E[x]clude unwanted files from being added to the compressed archive:

`zip -r {{compressed.zip}} {{path/to/dir}} -x \*.git\* \*node_modules\* ...`

- Package and compress multiple directories and files:

`zip -r {{compressed.zip}} {{/path/to/dir1 /path/to/dir2 /path/to/file}}`

- Add files to an existing zip file:

`zip {{compressed.zip}} {{path/to/file}}`

- Delete files from an existing zip file:

`zip -d {{compressed.zip}} "{{foo/*.tmp}}"`
