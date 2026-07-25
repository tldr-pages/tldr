# pvenode config

> Get and set node configuration.
> More information: <https://pve.proxmox.com/pve-docs/pvenode.1.html#cli_pvenode_config_get>.

- Display the whole configuration located in `/etc/pve/nodes/node_name/config`:

`pvenode {{[co|config]}} {{[g|get]}}`

- Display a specific property:

`pvenode {{[co|config]}} {{[g|get]}} --property {{property_name}}`

- Set the node description shown in the "Notes" tab:

`pvenode {{[co|config]}} {{[s|set]}} --description {{description_text}}`

- Set the location information of a node:

`pvenode {{[co|config]}} {{[s|set]}} --location latitude={{latitude}},longitude={{longitude}}`

- Delete a setting:

`pvenode {{[co|config]}} {{[s|set]}} --delete {{property_name}}`
