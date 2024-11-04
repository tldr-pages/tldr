# vgremove

> Remove volume group(s) in LVM.
> More information: <https://www.man7.org/linux/man-pages/man8/vgremove.8.html>.

- Remove a volume group with confirmation:

`vgremove my_volume_group`

- Forcefully remove a volume group without confirmation:

`vgremove --force my_volume_group`

- Set the debug level for detailed logging (level 2):

`vgremove --debug 2 my_volume_group`

- Use a specific config setting to override defaults:

`vgremove --config 'global/locking_type=1' my_volume_group`

- Display help text for usage information:

`vgremove --help`
