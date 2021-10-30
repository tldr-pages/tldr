# fdisk

> A program for managing partition tables and partitions on a hard disk.
> See also: `partprobe`.
> More information: <https://manned.org/fdisk>.

- List partitions:

`sudo fdisk -l`

- Start the partition manipulator:

`sudo fdisk {{/dev/sdX}}`

- Once partitioning a disk, create a partition:

`n`

- Once partitioning a disk, select a partition to delete:

`d`

- Once partitioning a disk, view the partition table:

`p`

- Once partitioning a disk, write the changes made:

`w`

- Once partitioning a disk, discard the changes made:

`q`

- Once partitioning a disk, open a help menu:

`m`
