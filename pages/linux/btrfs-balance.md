# btrfs balance

> Balance block groups on a btrfs filesystem.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>.

- Show the status of a running or paused balance operation:

`sudo btrfs balance status {{path/to/btrfs_filesystem}}`

- Balance all block groups (slow; rewrites all blocks in filesystem):

`sudo btrfs balance start {{path/to/btrfs_filesystem}}`

- Balance data block groups which are less than 15% utilized, running the operation in the background:

`sudo btrfs balance start --bg -dusage={{15}} {{path/to/btrfs_filesystem}}`

- Balance a max of 10 metadata chunks with less than 20% utilization and at least 1 chunk on a given device `devid` (see `btrfs filesystem show`):

`sudo btrfs balance start -musage={{20}},limit={{10}},devid={{devid}} {{path/to/btrfs_filesystem}}`

- Convert data blocks to the raid6 and metadata to raid1c3 (see mkfs.btrfs(8) for profiles):

`sudo btrfs balance start -dconvert={{raid6}} -mconvert={{raid1c3}} {{path/to/btrfs_filesystem}}`

- Convert data blocks to raid1, skipping already converted chunks (e.g. after a previous cancelled conversion operation):

`sudo btrfs balance start -dconvert={{raid1}},soft {{path/to/btrfs_filesystem}}`

- Cancel, pause, or resume a running or paused balance operation:

`sudo btrfs balance {{cancel|pause|resume}} {{path/to/btrfs_filesystem}}`
