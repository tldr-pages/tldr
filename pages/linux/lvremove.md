# lvremove

> Remove logical volumes.
> See also: `lvm`.
> More information: <https://manned.org/lvremove>.

- Remove a logical volume in a volume group:

`sudo lvremove {{volume_group}}/{{logical_volume}}`

- Remove all logical volumes in a volume group:

`sudo lvremove {{volume_group}}`
