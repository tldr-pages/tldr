# pvenode config

> Set and get node configuration.
> More information: <https://pve.proxmox.com/pve-docs/pvenode.1.html#cli_pvenode_config_get>.

- Print the whole configuration located in `/etc/pve/nodes/node_name/config`:

`pvenode config get`

- Print a specific property:

`pvenode config get --property {{property_name}}`

- Set the node description shown in the "Notes" tab:

`pvenode config set --description {{description_text}}`

- Set the location information of a node:

`pvenode config set --location latitude={{latitude}},longitude={{longitude}}`

- Delete a setting:

`pvenode config set --delete {{property_name}}`
