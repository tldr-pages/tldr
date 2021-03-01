# lvm

> Manage physical volumes, volume groups, and logical volumes using the Logical Volume Manager (LVM) interactivce shell.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logical_volumes/>.

- Start the Logical Volume Manager interactive shell:

`sudo lvm`

- List the Logical Volume Manager commands:

`sudo lvm help`

- Initialize /dev/sda1 to be used as a physical volume:

`sudo lvm pvcreate {{/dev/sda1}}`

- Display information about physcial volumes:

`sudo lvm pvdisplay`

- Create a volume group called vg1 from the physical volume on /dev/sda1:

`sudo lvm vgcreate {{vg1}} {{/dev/sda1}}`

- Display information about volume groups:

`sudo lvm vgdisplay`

- Create a logical volume with size 10G from volume group vg1:

`sudo lvm lvcreate -L {{10G}} {{vg1}}`

- Display information about logical volumes:

`sudo lvm lvdisplay`
