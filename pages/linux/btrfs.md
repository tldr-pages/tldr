# btrfs

> A filesystem based on the copy-on-write (COW) principle for Linux.
> This command also has documentation about its subcommands, e.g. `btrfs device`.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

- Create subvolume:

`sudo btrfs subvolume create {{path/to/subvolume}}`

- List subvolumes:

`sudo btrfs subvolume list {{path/to/mount_point}}`

- Show space usage information:

`sudo btrfs filesystem df {{path/to/mount_point}}`

- Enable quota:

`sudo btrfs quota enable {{path/to/subvolume}}`

- Show quota:

`sudo btrfs qgroup show {{path/to/subvolume}}`
