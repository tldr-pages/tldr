# sfdisk

> Display or manipulate a disk partition table.
> More information: <https://manned.org/sfdisk>.

- Back up the partition layout to a file:

`sudo sfdisk -d {{path/to/device}} > sda.dump`

- Restore a partition layout:

`sudo sfdisk /dev/sda < sda.dump`
