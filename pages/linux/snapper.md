# snapper

> Filesystem snapshot management tool.

- List snapshot configs:

`snapper list-configs`

- Create snapper config:

`snapper -c {{config}} create-config {{path/to/directory}}`

- Create snapshot and give description:

`snapper -c {{config}} create -d {{"snapshot description"}}`

- List snapshots for a config:

`snapper -c {{config}} list`

- Delete a snapshot:

`snapper -c {{config}} delete {{snapshot_number}}`

- Delete a range of snapshots:

`snapper -c {{config}} delete {{snapshot_X}}-{{snapshot_Y}}`
