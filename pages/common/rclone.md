# rclone

> CLI program to copy/sync/move files and directories to and from many cloud services.

- List contents of a folder on an rclone remote:

`rclone lsf {{remote_name}}:{{path/to/folder}}`

- Copy file or folder from local source to remote destination:

`rclone copy {{path/to/source_file_or_folder}} {{remote_name}}:{{path/to/destination_folder}}`

- Copy file or folder from remote source to local destination:

`rclone copy {{remote_name}}:{{path/to/source_file_or_folder}} {{path/to/destination_folder}}`

- Sync local source to remote destination, changing the destination only:

`rclone sync {{path/to/file_or_folder}} {{remote_name}}:{{path/to/folder}}`

- Move file or folder from local source to remote destination:

`rclone move {{path/to/file_or_folder}} {{remote_name}}:{{path/to/folder}}`

- Delete remote file or folder (use `--dry-run` to test, remove it to actually delete):

`rclone --dry-run delete {{remote_name}}:{{path/to/file_or_folder}}`

- Mount rclone remote (experimental):

`rclone mount {{remote_name}}:{{path/to/folder}} {{path/to/mount_point}}`

- Unmount rclone remote if CTRL-C fails (experimental):

`fusermount -u {{path/to/mount_point}}`
