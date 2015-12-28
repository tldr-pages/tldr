# zip

> Package and compress (archive) files into zip file

- package and compress multiple directories and files

`zip -r {{compressed.zip}} {{/path/to/dir1 /path/to/dir2 /path/to/file}}`

- add files to an existing zip file

`zip {{compressed.zip}} {{path/to/file}}`

- remove unwanted files from an existing zip file

`zip -d {{compressed.zip}} "{{foo/*.tmp}}"`
