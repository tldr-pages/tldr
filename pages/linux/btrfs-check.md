# btrfs check

> Check or repair a btrfs filesystem.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-check>.

- Check a btrfs filesystem:

`sudo btrfs check {{path/to/partition}}`

- Check and repair a btrfs filesystem (dangerous):

`sudo btrfs check --repair {{path/to/partition}}`

- Show the progress of the check:

`sudo btrfs check --progress {{path/to/partition}}`

- Verify the checksum of each data block (if the filesystem is good):

`sudo btrfs check --check-data-csum {{path/to/partition}}`

- Use the `n`-th superblock (`n` can be 0, 1 or 2):

`sudo btrfs check --super {{n}} {{path/to/partition}}`

- Rebuild the checksum tree:

`sudo btrfs check --repair --init-csum-tree {{path/to/partition}}`

- Rebuild the extent tree:

`sudo btrfs check --repair --init-extent-tree {{path/to/partition}}`
