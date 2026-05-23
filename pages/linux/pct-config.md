# pct config

> Print the configuration of a container.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_config>.

- Display the saved configuration:

`pct config {{container_id}}`

- Display the running configuration without pending changes:

`pct config {{container_id}} --current`

- Display configuration of a specific snapshot:

`pct config {{container_id}} --snapshot {{snapshot_name}}`
