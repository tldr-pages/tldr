# filen

> An end-to-end encrypted cloud storage service.
> More information: <https://github.com/FilenCloudDienste/filen-cli>.

- Upload a local file to a specific remote folder:

`filen upload --path {{path/to/local_file}} --remote {{remote_folder_id}}`

- Download a file or folder using its remote ID:

`filen download --id {{remote_id}} --path {{local_destination_path}}`

- List files and folders inside a remote folder:

`filen list --folder {{remote_folder_id}}`

- Delete a remote file or folder (move it to trash):

`filen rm --id {{remote_id}}`

- Restore a trashed item:

`filen trash restore --id {{remote_id}}`

- Permanently delete a trashed item:

`filen trash delete --id {{remote_id}}`

- Synchronize a local folder with a remote folder (one-way sync):

`filen sync --source {{local_folder}} --target {{remote_folder_id}}`

- Download changes from the cloud to a local folder (reverse sync):

`filen sync --source {{remote_folder_id}} --target {{local_folder}} --reverse`
