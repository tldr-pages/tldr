# btrfs check

> Check or repair a btrfs filesystem.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-check>.

- Check a btrfs filesystem:

`sudo btrfs check {{path/to/device}}`

- Check and repair a btrfs filesystem (dangerous):

`sudo btrfs check --repair {{path/to/device}}`

- Show progress during check:

`sudo btrfs check -p {{path/to/device}}`

- Verify data blocks' checksum (if filesystem is good):

`sudo btrfs check --check-data-csum {{path/to/device}}`

- Use the `n`-th superblock (`n` can be 0, 1 or 2):

`sudo btrfs check -s {{n}} {{path/to/device}}`

- Rebuild checksum tree:

`sudo btrfs check --repair --init-csum-tree {{path/to/device}}`

- Rebuild extent tree:

`sudo btrfs check --repair --init-extent-tree {{path/to/device}}`
