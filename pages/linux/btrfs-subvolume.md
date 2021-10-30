# btrfs subvolume

> Manage btrfs subvolumes and snapshots.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-subvolume>.

- Create a new empty subvolume:

`sudo btrfs subvolume create {{path/to/new_subvolume}}`

- List all subvolumes and snapshots in the specified filesystem:

`sudo btrfs subvolume list {{path/to/btrfs_filesystem}}`

- Delete a subvolume:

`sudo btrfs subvolume delete {{path/to/subvolume}}`

- Create a read-only snapshot of an existing subvolume:

`sudo btrfs subvolume snapshot -r {{path/to/source_subvolume}} {{path/to/target}}`

- Create a read-write snapshot of an existing subvolume:

`sudo btrfs subvolume snapshot {{path/to/source_subvolume}} {{path/to/target}}`

- Show detailed information about a subvolume:

`sudo btrfs subvolume show {{path/to/subvolume}}`
