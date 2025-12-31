# btrfs filesystem

> Manage btrfs filesystems.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- Show filesystem usage (optionally run as root to show detailed information):

`btrfs {{[f|filesystem]}} {{[u|usage]}} {{path/to/btrfs_mount}}`

- Show usage by individual devices:

`sudo btrfs {{[f|filesystem]}} {{[sh|show]}} {{path/to/btrfs_mount}}`

- Defragment a single file on a btrfs filesystem (avoid while a deduplication agent is running):

`sudo btrfs {{[f|filesystem]}} {{[de|defragment]}} {{[-v|--verbose]}} {{path/to/file}}`

- Defragment a directory recursively (does not cross subvolume boundaries):

`sudo btrfs {{[f|filesystem]}} {{[de|defragment]}} {{[-v|--verbose]}} -r {{path/to/directory}}`

- Force syncing unwritten data blocks to disk(s):

`sudo btrfs {{[f|filesystem]}} {{[sy|sync]}} {{path/to/btrfs_mount}}`

- Summarize disk usage for the files in a directory recursively:

`sudo btrfs {{[f|filesystem]}} du {{[-s|--summarize]}} {{path/to/directory}}`

- Create a swap file:

`sudo btrfs {{[f|filesystem]}} {{[m|mkswapfile]}} --size {{8g}} --uuid {{clear|random|time|UUID_value}} {{path/to/swapfile}}`
