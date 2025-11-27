# pvesh

> Interface with the Proxmox VE API.
> More information: <https://pve.proxmox.com/pve-docs/pvesh.1.html>.

- List available nodes:

`pvesh {{[g|get]}} /nodes`

- Display detailed information about containers or virtual machines:

`pvesh {{[g|get]}} /nodes/{{node_name}}/{{lxc|qemu}}`

- Discover API paths:

`pvesh {{[l|ls]}} {{/}}`

- Display API path usage instructions:

`pvesh {{[u|usage]}} {{/pools}}`

- Add a new thinpool to Proxmox:

`pvesh create /storage --storage {{volume_id}} --vgname {{volume_group}} --type lvmthin --thinpool {{thinpool_name}} --content {{content_type1,content_type2,...}}`
