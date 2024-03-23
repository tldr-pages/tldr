# snapper

> Filesystem snapshot management tool.
> More information: <http://snapper.io/manpages/snapper.html>.

- List snapshot configs:

`snapper list-configs`

- Create snapper config:

`snapper -c {{config}} create-config {{path/to/directory}}`

- Create a snapshot with a description:

`snapper -c {{config}} create -d "{{snapshot_description}}"`

- List snapshots for a config:

`snapper -c {{config}} list`

- Delete a snapshot:

`snapper -c {{config}} delete {{snapshot_number}}`

- Delete a range of snapshots:

`snapper -c {{config}} delete {{snapshot1}}-{{snapshot2}}`
