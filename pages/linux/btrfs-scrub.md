# btrfs scrub

> Scrub btrfs filesystems to verify data integrity.
> It is recommended to run a scrub once a month.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Start a scrub:

`sudo btrfs scrub start {{path/to/btrfs_mount}}`

- Show the status of an ongoing or last completed scrub:

`sudo btrfs scrub status {{path/to/btrfs_mount}}`

- Cancel an ongoing scrub:

`sudo btrfs scrub cancel {{path/to/btrfs_mount}}`

- Resume a previously cancelled scrub:

`sudo btrfs scrub resume {{path/to/btrfs_mount}}`

- Start a scrub, but wait until the scrub finishes before exiting:

`sudo btrfs scrub start -B {{path/to/btrfs_mount}}`

- Start a scrub in quiet mode (does not print errors or statistics):

`sudo btrfs scrub start -q {{path/to/btrfs_mount}}`
