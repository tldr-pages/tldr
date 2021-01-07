# btrfs filesystem

> Manage btrfs filesystems.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-filesystem>.

- Show filesystem usage (optionally run as root to show detailed information):

`btrfs filesystem usage {{path/to/btrfs_mount}}`

- Show usage by individual devices:

`btrfs filesystem show {{path/to/btrfs_mount}}`

- Defragment a single file on a btrfs filesystem:

`sudo btrfs filesystem defragment {{path/to/file}}`

- Defragment a directory recursively (does not cross subvolume boundaries):

`sudo btrfs filesystem defragment -r {{path/to/directory}}`

- Force syncing unwritten data blocks to disk(s):

`sudo btrfs filesystem sync {{path/to/btrfs_mount}}`

- Summarize disk usage for the files in a directory recursively:

`sudo btrfs filesystem du {{path/to/directory}}`
