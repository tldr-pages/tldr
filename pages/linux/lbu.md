# lbu

> Manage `apk` overlay files on a diskless Alpine Linux system.
> Note: Subcommands like `include` write to `/etc`, which is stored in RAM. You need to run `lbu commit` to save the changes.
> More information: <https://wiki.alpinelinux.org/wiki/Alpine_local_backup>.

- Commit changes to persistent storage (only files in `/etc` by default):

`lbu {{[ci|commit]}}`

- List files that would be saved using `commit`:

`lbu {{[st|status]}}`

- Display changes in tracked files that would be saved using `commit`:

`lbu diff`

- Include a specific file or directory in the `apk` overlay:

`lbu {{[inc|include]}} {{path/to/file_or_directory}}`

- Exclude a specific file or directory in `/etc` from the `apk` overlay:

`lbu {{[ex|exclude]}} {{path/to/file_or_directory}}`

- Display the list of manually included/excluded files:

`lbu {{include|exclude}} -l`

- List backups (previously created overlays):

`lbu {{[lb|list-backup]}}`

- Revert to a backup overlay:

`lbu revert {{overlay_filename.tar.gz}}`
