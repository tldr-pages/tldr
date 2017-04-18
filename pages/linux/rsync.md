# rsync

> Remote and local file synchronization tool

 - Synchronize two folders recursively:

 `rsync -r {{source_folder}}/ {{destination_folder}}/`

 - Update the destination with added/changed files from source:

 `rsync -r --update {{source_folder}}/ {{destination_folder}}/`

 - Synchronize a local folder with a remote destination via SSH and deleting extra files in destination:

 `rsync -r --delete {{source_folder}}/ {{root@server:/destination_folder}}/`

 - Mirror source to destination, including ownership, groups, mask, timestamps:

 `rsync -a --delete {{source_folder}}/ {{destination_folder}}/`

 - Test run a destructive mirror operation, show progress, human readable numbers and exclude any dot files:

 `rsync -ahv --dry-run --progress --delete --exclude=".*" {{source_folder}}/ {{root@server:/destination_folder}}/`
