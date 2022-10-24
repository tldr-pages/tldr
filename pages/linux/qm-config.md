# qm config

> Display the virtual machine configuration with pending configuration changes applied.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Display the virtual machine configuration:

`qm config {{vm_id}}`

- Display the current configuration values instead of pending values for the virtual machine:

`qm config --current {{true}} {{vm_id}}`

- Fetch the configuration values from the given snapshot:

`qm config --snapshot {{snapshot_name}} {{vm_id}}`
