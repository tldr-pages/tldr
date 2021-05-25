# btrfs filesystem

> Manage btrfs filesystems.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-filesystem>.

- Show filesystem usage (optionally run as root to show detailed information):

`btrfs filesystem usage {{path/to/btrfs_mount}}`

- Show usage by individual devices:

`sudo btrfs filesystem show {{path/to/btrfs_mount}}`

- Defragment a single file on a btrfs filesystem (avoid while a deduplication agent is running):

`sudo btrfs filesystem defragment -v {{path/to/file}}`

- Defragment a directory recursively (does not cross subvolume boundaries):

`sudo btrfs filesystem defragment -v -r {{path/to/directory}}`

- Force syncing unwritten data blocks to disk(s):

`sudo btrfs filesystem sync {{path/to/btrfs_mount}}`

- Summarize disk usage for the files in a directory recursively:

`sudo btrfs filesystem du --summarize {{path/to/directory}}`
