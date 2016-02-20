# zip

> Package and compress (archive) files into zip file.

- Package and compress multiple directories and files:

`zip -r {{compressed.zip}} {{/path/to/dir1 /path/to/dir2 /path/to/file}}`

- Add files to an existing zip file:

`zip {{compressed.zip}} {{path/to/file}}`

- Remove unwanted files from an existing zip file:

`zip -d {{compressed.zip}} "{{foo/*.tmp}}"`

- Remove unwanted pattern files from target dirs:

`zip -r {{compressed.zip}} {{target_dirs}} -x \*.git\* \*node_modules\* ...`
