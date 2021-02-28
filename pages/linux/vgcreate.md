# vgcreate

> Create volume groups combining multiple mass-storage devices.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/logical_volume_manager_administration>.

- Create a new volume group called vg1 using the `/dev/sda1` device:

`vgcreate {{vg1}} {{/dev/sda1}}`

- Create a new volume group called vg1 using multiple devices:

`vgcreate {{vg1}} {{/dev/sda1}} {{/dev/sdb1}} {{/dev/sdc1}}`
