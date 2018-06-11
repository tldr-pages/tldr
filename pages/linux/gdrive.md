# gdrive

> Terminal tool for Google Drive operations. Folder/file id can be obtained from the Google Drive folder or id url.

- Upload path to -p parent folder using it's id:

`gdrive upload -p {{id}} {{path}}`

- Download file or directory by id:

`gdrive download {{id}}`

- Download file or directory by id to local --p path:

`gdrive download --p {{path}} {{id}}`

- Create revision of 'id' file using file specified by 'path':

`gdrive update {{id}} {{path}}`
