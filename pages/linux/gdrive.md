# gdrive

> Terminal tool for Google Drive operations. Folder/file id can be obtained from the Google Drive folder or id url.

- Upload local 'path' to -p 'id' parent folder:

`gdrive upload -p {{id}} {{path}}`

- Download file or directory by 'id' to current path:

`gdrive download {{id}}`

- Download file or directory by id to local --p 'path':

`gdrive download --p {{path}} {{id}}`

- Create revision of 'id' file using file specified by 'path':

`gdrive update {{id}} {{path}}`
