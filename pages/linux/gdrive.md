# gdrive

> Terminal tool for Google Drive operations.
> Folder/file id can be obtained from the Google Drive folder or id url.

- Upload a local path to the parent folder with the specified id:

`gdrive upload -p {{id}} {{path}}`

- Download file or directory by id to current path:

`gdrive download {{id}}`

- Download a file or directory by its id to a local path:

`gdrive download --p {{path}} {{id}}`

- Create revision of id file using file specified by path:

`gdrive update {{id}} {{path}}`
