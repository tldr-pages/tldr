# btrfs scrub

> Scrub btrfs filesystems to verify data integrity.
> It is recommended to run a scrub once a month.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Start a scrub:

`sudo btrfs {{[sc|scrub]}} start {{path/to/btrfs_mount}}`

- Show the status of an ongoing or last completed scrub:

`sudo btrfs {{[sc|scrub]}} status {{path/to/btrfs_mount}}`

- Cancel an ongoing scrub:

`sudo btrfs {{[sc|scrub]}} {{[c|cancel]}} {{path/to/btrfs_mount}}`

- Resume a previously cancelled scrub:

`sudo btrfs {{[sc|scrub]}} {{[r|resume]}} {{path/to/btrfs_mount}}`

- Start a scrub, but do not put the program in the [B]ackground:

`sudo btrfs {{[sc|scrub]}} start -B {{path/to/btrfs_mount}}`

- Start a scrub in quiet mode (does not print errors or statistics):

`sudo btrfs {{[sc|scrub]}} start {{[-q|--quiet]}} {{path/to/btrfs_mount}}`
