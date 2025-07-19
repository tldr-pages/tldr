# btrfs check

> Check or repair a btrfs filesystem.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Check a btrfs filesystem:

`sudo btrfs {{[c|check]}} {{path/to/partition}}`

- Check and repair a btrfs filesystem (dangerous):

`sudo btrfs {{[c|check]}} --repair {{path/to/partition}}`

- Show the progress of the check:

`sudo btrfs {{[c|check]}} {{[-p|--progress]}} {{path/to/partition}}`

- Verify the checksum of each data block (if the filesystem is good):

`sudo btrfs {{[c|check]}} --check-data-csum {{path/to/partition}}`

- Use the `n`-th superblock (`n` can be 0, 1 or 2):

`sudo btrfs {{[c|check]}} {{[-s|--super]}} {{n}} {{path/to/partition}}`

- Rebuild the checksum tree:

`sudo btrfs {{[c|check]}} --repair --init-csum-tree {{path/to/partition}}`

- Rebuild the extent tree:

`sudo btrfs {{[c|check]}} --repair --init-extent-tree {{path/to/partition}}`
