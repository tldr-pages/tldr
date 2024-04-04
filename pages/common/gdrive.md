# gdrive

> Interact with Google Drive.
> Folder/file ID can be obtained from the Google Drive folder or ID URL.
> More information: <https://github.com/gdrive-org/gdrive>.

- Upload a local path to the parent folder with the specified ID:

`gdrive upload -p {{id}} {{path/to/file_or_folder}}`

- Download file or directory by ID to current directory:

`gdrive download {{id}}`

- Download to a given local path by its ID:

`gdrive download --path {{path/to/folder}} {{id}}`

- Create a new revision of an ID using a given file or folder:

`gdrive update {{id}} {{path/to/file_or_folder}}`
