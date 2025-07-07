# filen

> An end-to-end encrypted cloud storage service.
> More information: <https://github.com/FilenCloudDienste/filen-cli>.

- Upload a local file to a specific remote folder:

`filen upload {{path/to/local_file}} {{remote_folder_id}}`

- Download a file or folder using its remote ID:

`filen download {{remote_id}} {{local_destination_path}}`

- List files and folders inside a remote folder:

`filen ls {{remote_folder_id}}`

- Delete a remote file or folder (move it to trash):

`filen rm {{remote_id}}`

- Restore a trashed item:

`filen trash restore {{remote_id}}`

- Permanently delete a trashed item:

`filen trash delete {{remote_id}}`

- Synchronize a local folder with a remote folder (two-way sync):

`filen sync {{local_folder}}:/{{remote_folder_id}} --continuous`

- Download changes from the cloud to a local folder (one-way sync):

`filen sync {{local_folder}}:ctl:/{{remote_folder_id}}`
