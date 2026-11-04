# pvesm add

> Add storages.
> More information: <https://pve.proxmox.com/pve-docs/pvesm.1.html#cli_pvesm_add>.

- Add a directory storage:

`pvesm {{[ad|add]}} dir {{storage_name}} --path {{path/to/directory}}`

- Add an LVM storage:

`pvesm {{[ad|add]}} lvm {{storage_name}} --vgname {{volume_group_name}}`

- Add an LVM-Thin storage:

`pvesm {{[ad|add]}} lvmthin {{storage_name}} --vgname {{volume_group_name}} --thinpool {{logical_volume_name}}`
