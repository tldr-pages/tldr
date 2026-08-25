# vgcreate

> Create volume groups combining multiple mass-storage devices.
> See also: `lvm`.
> More information: <https://manned.org/vgcreate>.

- Create a new volume group using the specified device:

`sudo vgcreate {{volume_group}} {{/dev/sdXY}}`

- Create a new volume group using multiple devices:

`sudo vgcreate {{volume_group}} {{/dev/sdXY /dev/sdXZ ...}}`

- Create a new volume group with custom physical extent size:

`sudo vgcreate {{-s|--physicalextentsize}} {{8M}} {{volume_group}} {{/dev/sdXY /dev/sdXZ ...}}`
