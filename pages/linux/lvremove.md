# lvremove

> Remove one or more logical volumes.
> See also: `lvm`.
> More information: <https://man7.org/linux/man-pages/man8/lvremove.8.html>.

- Remove a logical volume in a volume group:

`sudo lvremove {{volume_group}}/{{logical_volume}}`

- Remove all logical volumes in a volume group:

`sudo lvremove {{volume_group}}`
