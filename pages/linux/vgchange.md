# vgchange

> Change the attributes of a Logical Volume Manager (LVM) volume group.
> See also: `lvm`.
> More information: <https://manned.org/vgchange>.

- Activate or deactivate logical volumes in all volume groups:

`sudo vgchange --activate {{y|n}}`

- Activate or deactivate logical volumes in the specified volume group (determine with `vgscan`):

`sudo vgchange --activate {{y|n}} {{vg}}}`
