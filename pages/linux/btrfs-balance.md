# btrfs balance

> Balance block groups on a btrfs filesystem
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-balance>.

- Show the status of a running or paused balance:

`sudo btrfs balance status {{path/to/btrfs_filesystem}}`

- Balance all block groups (slow; rewrites all blocks in filesystem):

`sudo btrfs balance start {{path/to/btrfs_filesystem}}`

- Balance data block groups less than 15% utilized (and run in background):

`sudo btrfs balance start --bg -dusage=15 {{path/to/btrfs_filesystem}}`

- Balance (max 10) metadata chunks with < 20% utilization and at least 1 chunk on device `devid` (`btrfs filesystem show`):

`sudo btrfs balance start -musage=20,limit=10,devid={{devid}} {{path/to/btrfs_filesystem}}`

- Convert data blocks to raid6 profile and metadata to raid1c3 (see mkfs.btrfs(8) for profiles):

`sudo btrfs balance start -dconvert=raid6 -mconvert=raid1c3 {{path/to/btrfs_filesystem}}`

- Convert data blocks to raid1 profile, skipping already converted chunks (e.g. after previous cancelled convert)

`sudo btrfs balance start -dconvert=raid1,soft {{path/to/btrfs_filesystem}}`

- Cancel/pause/resume a running or paused balance:

`sudo btrfs balance {{cancel|pause|resume}} {{path/to/btrfs_filesystem}}`
