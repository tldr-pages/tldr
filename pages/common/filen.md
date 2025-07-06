# filen

> Command-line interface for Filen, an end-to-end encrypted cloud storage service.
> Supports file upload/download, sync, trash management, mount a network drive and integration with S3 and WebDAV.
> Running the command without arguments opens an interactive mode.
> More information: <https://github.com/FilenCloudDienste/filen-cli>.

- Upload a local file to a specific remote folder:

`filen upload --path {{local_file_path}} --remote {{remote_folder_id}}`

- Download a file or folder using its remote ID:

`filen download --id {{remote_id}} --path {{local_destination_path}}`

- List files and folders inside a remote folder:

`filen list --folder {{remote_folder_id}}`

- Delete a remote file or folder (moves it to trash):

`filen rm --id {{remote_id}}`

- Restore a trashed item:

`filen trash restore --id {{remote_id}}`

- Permanently delete a trashed item:

`filen trash delete --id {{remote_id}}`

- Synchronize a local folder with a remote folder (one-way sync):

`filen sync --source {{local_folder}} --target {{remote_folder_id}}`

- Reverse sync: download changes from the cloud to a local folder:

`filen sync --source {{remote_folder_id}} --target {{local_folder}} --reverse`
