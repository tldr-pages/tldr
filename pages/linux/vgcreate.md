# vgcreate

> Create volume groups combining multiple mass-storage devices.
> See also: `lvm`.
> More information: <https://manned.org/vgcreate>.

- Create a new volume group using the specified device:

`sudo vgcreate {{volume_group}} {{/dev/sdXY}}`

- Create a new volume group using multiple devices:

`sudo vgcreate {{volume_group}} {{/dev/sdXY}} {{/dev/sdXZ}}`
