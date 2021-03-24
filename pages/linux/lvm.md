# lvm

> Manage physical volumes, volume groups, and logical volumes using the Logical Volume Manager (LVM) interactive shell.
> More information: <https://man7.org/linux/man-pages/man8/lvm.8.html>.

- Start the Logical Volume Manager interactive shell:

`sudo lvm`

- List the Logical Volume Manager commands:

`sudo lvm help`

- Initialize a drive or partition to be used as a physical volume:

`sudo lvm pvcreate {{/dev/sdXY}}`

- Display information about physcial volumes:

`sudo lvm pvdisplay`

- Create a volume group called vg1 from the physical volume on `/dev/sdXY`:

`sudo lvm vgcreate {{vg1}} {{/dev/sdXY}}`

- Display information about volume groups:

`sudo lvm vgdisplay`

- Create a logical volume with size 10G from volume group vg1:

`sudo lvm lvcreate -L {{10G}} {{vg1}}`

- Display information about logical volumes:

`sudo lvm lvdisplay`
