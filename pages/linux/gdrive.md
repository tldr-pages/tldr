# gdrive

> Command line tool to interact with Google Drive.
> Folder/file id can be obtained from the Google Drive folder or id url.

- Upload a local path to the parent folder with the specified id:

`gdrive upload -p {{id}} {{path/to/file_or_folder}}`

- Download file or directory by id to current path:

`gdrive download {{id}}`

- Download a file or directory by its id to a local path:

`gdrive download --path {{path/to/file_or_folder}} {{id}}`

- Create revision of id file using file specified by path:

`gdrive update {{id}} {{path/to/file_or_folder}}`
