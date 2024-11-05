# vgremove

> Remove volume group(s) in LVM.
> More information: <https://manned.org/vgremove>.

- Remove a volume group with confirmation:

`vgremove {{volume_group}}`

- Forcefully remove a volume group without confirmation:

`vgremove --force {{volume_group}}`

- Set the debug level for detailed logging (level 2):

`vgremove --debug 2 {{volume_group}}`

- Use a specific config setting to override defaults:

`vgremove --config '{{global/locking_type=1}}' {{volume_group}}`

- Display help text for usage information:

`vgremove --help`
