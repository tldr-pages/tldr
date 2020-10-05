# dumpe2fs

> Print the super block and blocks group information for ext2/ext3/ext4 filesystem.
> Unmount the partition before running this command using `umount {{device}}`.
> More information: <https://linux.die.net/man/8/dumpe2fs>.

- Display ext2, ext3 and ext4 filesystem information for the device `/dev/sda1`:

`dumpe2fs {{/dev/sda1}}`

- Display the blocks which are reserved as bad in the filesystem:

`dumpe2fs -b {{/dev/sda1}}`

- Force display filesystem information even with non-recogonisable feature flags:

`dumpe2fs -f {{/dev/sda1}}`

- Only display the superblock information and not any of the block group descriptor detail information:

`dumpe2fs -h {{/dev/sda1}}`

- Print the detailed group information block numbers in hexadecimal format:

`dumpe2fs -x {{/dev/sda1}}`
