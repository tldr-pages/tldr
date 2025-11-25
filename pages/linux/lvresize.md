# lvresize

> Change the size of a logical volume.
> See also: `lvm`.
> More information: <https://manned.org/lvresize>.

- Change the size of a logical volume to 120 GB:

`sudo lvresize {{[-L|--size]}} 120G {{volume_group}}/{{logical_volume}}`

- Extend the size of a logical volume as well as the underlying filesystem by 120 GB:

`sudo lvresize {{[-L|--size]}} +120G {{[-r|--resizefs]}} {{volume_group}}/{{logical_volume}}`

- Extend the size of a logical volume to 100% of the free physical volume space:

`sudo lvresize {{[-l|--extents]}} 100%FREE {{volume_group}}/{{logical_volume}}`

- Reduce the size of a logical volume as well as the underlying filesystem by 120 GB:

`sudo lvresize {{[-L|--size]}} -120G {{[-r|--resizefs]}} {{volume_group}}/{{logical_volume}}`
