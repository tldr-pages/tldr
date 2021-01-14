# e2undo

> Replay undo logs for an ext2/ext3/ext4 filesystem.
> This can be used to undo a failed operation by an e2fsprogs program.
> More information: <https://man7.org/linux/man-pages/man8/e2undo.8.html>.

- Display information about a specific undo file:

`e2undo -h {{path/to/undo_file}} {{/dev/sdXN}}`

- Perform a dry-run and display the candidate blocks for replaying:

`e2undo -nv {{path/to/undo_file}} {{/dev/sdXN}}`

- Perform an undo operation:

`e2undo {{path/to/undo_file}} {{/dev/sdXN}}`

- Perform an undo operation and display verbose information:

`e2undo -v {{path/to/undo_file}} {{/dev/sdXN}}`

- Write the old contents of the block to an undo file before overwriting a file system block:

`e2undo -z {{path/to/file.e2undo}} {{path/to/undo_file}} {{/dev/sdXN}}`
