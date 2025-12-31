# pct config

> Print the configuration of a container.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_config>.

- Display the saved configuration:

`pct config {{100}}`

- Display the running configuration without pending changes:

`pct config {{100}} --current`

- Display configuration of a specific snapshot:

`pct config {{100}} --snapshot {{snapshot_name}}`
