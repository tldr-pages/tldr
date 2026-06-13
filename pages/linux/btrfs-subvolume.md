# btrfs subvolume

> Manage btrfs subvolumes and snapshots.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Create a new empty subvolume:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{path/to/new_subvolume}}`

- List all subvolumes and snapshots in the specified filesystem:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{path/to/btrfs_filesystem}}`

- Delete a subvolume:

`sudo btrfs {{[su|subvolume]}} {{[d|delete]}} {{path/to/subvolume}}`

- Create a [r]ead-only snapshot of an existing subvolume:

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} -r {{path/to/source_subvolume}} {{path/to/target}}`

- Create a read-write snapshot of an existing subvolume:

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} {{path/to/source_subvolume}} {{path/to/target}}`

- Show detailed information about a subvolume:

`sudo btrfs {{[su|subvolume]}} {{[sh|show]}} {{path/to/subvolume}}`
