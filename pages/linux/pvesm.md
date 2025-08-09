# pvesm

> Manage Proxmox storage.
> More information: <https://pve.proxmox.com/pve-docs/pvesm.1.html>.

- Get status for all datastores:

`pvesm status`

- List storage contents:

`pvesm list {{storage_name}}`

- Add a directory storage:

`pvesm add dir {{storage_name}} --path {{path/to/directory}}`

- Remove a storage:

`pvesm remove {{storage_name}}`
