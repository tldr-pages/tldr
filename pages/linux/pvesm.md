# pvesm

> Manage Proxmox storage.
> More information: <https://pve.proxmox.com/pve-docs/pvesm.1.html>.

- Get status for all datastores:

`pvesm {{[st|status]}}`

- List storage contents:

`pvesm {{[l|list]}} {{storage_name}}`

- Add a directory storage:

`pvesm add {{[d|dir]}} {{storage_name}} --path {{path/to/directory}}`

- Set a storage to contain specific content:

`pvesm set {{storage_name}} --content {{iso,images,backup,vztmpl,...}}`

- Delete a file from storage:

`pvesm free {{local:iso/archlinux-2025.08.01-x86_64.iso}}`

- Remove a storage:

`pvesm {{[r|remove]}} {{storage_name}}`
