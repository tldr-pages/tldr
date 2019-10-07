# btrfs

> A modern copy on write (CoW) filesystem for Linux.

- Create subvolume:

`sudo btrfs subvolume create {{path/to/subvolume}}`

- List subvolume:

`sudo btrfs subvolume list {{path/to/moount_point}}`

- Show space usage information:

`sudo btrfs filesystem df {{path/to/mount_point}}`

- Enable quota:

`sudo btrfs quota enable {{path/to/subvolume}}`

- Show quota:

`sudo btrfs qgroup show {{path/to/subvolume}}`
