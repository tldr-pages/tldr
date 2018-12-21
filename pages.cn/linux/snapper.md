# snapper

> Filesystem snapshot management tool.

- List snapshot configs:

`snapper list-configs`

- Create snapper config:

`snapper -c {{config}} create-config {{path/to/directory}}`

- List snapshots for a config:

`snapper -c {{config}} list`

- Create a new snapshot:

`snapper -c {{config}} snapshot`

- Delete a snapshot:

`snapper -c {{config}} delete {{snapshot_number}}`

- Delete a range of snapshots:

`snapper -c {{config}} delete {{snapshot_X}}-{{snapshot_Y}}`
