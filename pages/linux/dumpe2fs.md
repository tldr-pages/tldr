# dumpe2fs

> Print the super block and blocks group information for ext2/ext3/ext4 filesystems.
> Unmount the partition before running this command using `umount {{device}}`.
> More information: <https://manned.org/dumpe2fs>.

- Display ext2, ext3 and ext4 filesystem information:

`dumpe2fs {{/dev/sdXN}}`

- Display the blocks which are reserved as bad in the filesystem:

`dumpe2fs -b {{/dev/sdXN}}`

- Force display filesystem information even with unrecognizable feature flags:

`dumpe2fs -f {{/dev/sdXN}}`

- Only display the superblock information and not any of the block group descriptor detail information:

`dumpe2fs -h {{/dev/sdXN}}`

- Print the detailed group information block numbers in hexadecimal format:

`dumpe2fs -x {{/dev/sdXN}}`
