# lvremove

> Remove one or more logical volumes.
> More information: <https://sourceware.org/lvm2/>.

- Remove a logical volume in a volume group:

`sudo lvremove {{volume_group}}/{{logical_volume}}`

- Remove all logical volumes in a volume group:

`sudo lvremove {{volume_group}}`
