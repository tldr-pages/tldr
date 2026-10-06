# btrfs send

> Transfer data (subvolume/snapshot) from one filesystem to another in a streamable format.
> Note: `send` requires the snapshot be read-only.
> See also: `btrfs-subvolume`, `btrfs-property`.
> More information: <https://btrfs.readthedocs.io/en/latest/Send-receive.html>.

- Send a subvolume snapshot to a file instead of `stdout`:

`sudo btrfs send -f {{path/to/file.btrfs}} {{path/to/source_snapshot}}`

- Restore a subvolume snapshot from a file instead of `stdin`:

`sudo btrfs receive -f {{path/to/file.btrfs}} {{path/to/destination_directory}}`

- Send a subvolume snapshot stream and pipe it to a receiving destination:

`sudo btrfs send {{path/to/source_snapshot}} | sudo btrfs receive {{path/to/destination_directory}}`

- Send an incremental update (differences between parent and new snapshot) to a file:

`sudo btrfs send -p {{path/to/parent_snapshot}} -f {{path/to/incremental.btrfs}} {{path/to/new_snapshot}}`

- Send an incremental update stream and pipe it to a receiving destination:

`sudo btrfs send -p {{path/to/parent_snapshot}} {{path/to/new_snapshot}} | sudo btrfs receive {{path/to/destination_directory}}`

- Send a subvolume snapshot over SSH (the receiving `sudo` must be configured for passwordless execution):

`sudo btrfs send {{path/to/source_snapshot}} | ssh {{user}}@{{host}} "sudo btrfs receive {{path/to/destination_directory}}"`

- Dump stream metadata from a file without modifying the filesystem:

`sudo btrfs receive --dump -f {{path/to/file.btrfs}}`
