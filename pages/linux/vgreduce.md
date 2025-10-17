# vgreduce

> vgreduce allows you to remove one or more unused physical volumes from a volume group
> See also: `lvm`, `vgreduce`.
> More information: <https://linux.die.net/man/8/vgreduce>.

- Removes physical volume from volume group:

`sudo vgreduce [VOLUME_GROUP_NAME] [PHYSICAL_VOLUME_NAME]`

- Remove all empty physical volumes if none are given on command line:

`sudo vgremove -a [VOLUME_GROUP_NAME]`

- Removes all missing physical volumes from the volume group, if there are no logical volumes allocated on those. This resumes normal operation of the volume group (new logical volumes may again be created, changed and so on).If this is not possible (there are logical volumes referencing the missing physical volumes) and you cannot or do not want to remove them manually, you can run this option with --force to have vgreduce remove any partial LVs.

`sudo vgremove --removemissing [VOLUME_GROUP_NAME]`
