# vgremove

> Remove volume group(s) in LVM.
> More information: <https://manned.org/vgremove>.

- Remove a volume group with confirmation:

`sudo vgremove {{volume_group}}`

- Forcefully remove a volume group without confirmation:

`sudo vgremove {{[-f|--force]}} {{volume_group}}`

- Set the debug level for detailed logging to level 2, (repeat `--debug` up to 6 times to increase the level):

`sudo vgremove {{[-d|--debug]}} {{[-d|--debug]}} {{volume_group}}`

- Use a specific config setting to override defaults:

`sudo vgremove --config '{{global/locking_type=1}}' {{volume_group}}`

- Display help:

`vgremove {{[-h|--help]}}`
