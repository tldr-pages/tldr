# vgreduce

> Remove one or more unused physical volumes from a volume group.
> See also: `lvm`, `vgreduce`.
> More information: <https://linux.die.net/man/8/vgreduce>.

- Remove physical volume from volume group:

`sudo vgreduce {{volume_group}} {{volume_name}}`

- Remove all empty physical volumes if none are given on command line:

`sudo vgremove -a [VOLUME_GROUP_NAME]`

- Remove all missing physical volumes from the volume group, if there are no logical volumes allocated on those. If there are logical volumes referencing the missing physical volumes you can run this option with --force:

`sudo vgremove --removemissing [VOLUME_GROUP_NAME]`
