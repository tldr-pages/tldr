# fdisk

> Manipulate disk partition table.

- List  the  partition  tables for the sda disk and then exit:

`fdisk -l /dev/sda`

- Print the size (in blocks) of /dev/sda1:

`fdisk -s /dev/sda1`

- Create/remove/change partitions in the device:

`fdisk /dev/sda`

- Print help and then exit:

`fdisk -h`
