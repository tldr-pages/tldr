# gdrive

> Interact with Google Drive.
> Folder/file ID can be obtained from the Google Drive folder or ID URL.
> More information: <https://github.com/prasmussen/gdrive>.

- Upload a local path to the parent folder with the specified ID:

`gdrive upload {{[-p|--parent]}} {{folder_id}} {{path/to/file_or_folder}}`

- Download file or directory by ID to current directory:

`gdrive download {{file_or_directory_id}}`

- Download to a given local path by its ID:

`gdrive download --path {{path/to/folder}} {{file_or_directory_id}}`

- Create a new revision of an ID using a given file or folder:

`gdrive update {{file_or_folder_id}} {{path/to/file_or_folder}}`
