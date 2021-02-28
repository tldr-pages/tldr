# lvremove

> Remove one or more logical volumes.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/logical_volume_manager_administration/index>.

- Remove a logical volume in a volume group:

`sudo lvremove {{volume_group}}/{{logical_volume}}`

- Remove all logical volumes in a volume group:

`sudo lvremove {{volume_group}}`
