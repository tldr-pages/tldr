# btrfs send and receive

> Send and receive are complementary commands that allow to transfer data from one filesystem to another in a streamable format.
> See also: `btrfs-subvolume`, `btrfs-property`.
> More information: <https://btrfs.readthedocs.io/en/latest/Send-receive.html>.

- Send subvolume snapshot (must be `read-only`), written to a file (`-f`) instead of `STDOUT`:

`sudo btrfs send {{path/to/source_snapshot}} -f {{path/to/file.btrfs}}`

- Receive/unpack subvolume snapshot into destination:

`sudo btrfs receive -f {{path/to/file.btrfs}} {{path/to/destination_directory}}`

- Send and receive using a local pipe:

`sudo btrfs send {{path/to/source_snapshot}} | sudo btrfs receive {{path/to/destination_directory}}`

- Send and receive over SSH (the receiving `sudo` must be configured for passwordless execution):

`sudo btrfs send {{path/to/source_snapshot}} | ssh {{user}}@{{host}} "sudo btrfs receive {{path/to/destination_directory}}"`

- Send incremental stream (only differences between parent and new snapshot):

`sudo btrfs send -p {{path/to/parent_snapshot}} {{path/to/new_snapshot}} -f {{path/to/incremental.btrfs}}`
