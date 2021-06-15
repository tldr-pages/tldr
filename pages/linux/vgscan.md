# vgscan

> Scan for volume groups on all supported Logical Volume Manager (LVM) block devices.
> See also `lvm`, `vgchange`.
> More information: <https://manned.org/vgscan>.

- Scan for volume groups and print information about each group found:

`sudo vgscan`

- Scan for volume groups and add or remove the special files in `/dev` needed to access the logical volumes in a group:

`sudo vgscan --mknodes`
