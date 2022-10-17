# qm config

> Get the VM configurations with pending configuration changes applied. 
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Get the VM configurations with pending configuration changes applied:

`qm config {{vmid}}`

- Get the VM configurations without pending configuration changes applied:

`qm config {{vmid}} --current 1`

- Get the VM configurations of a snapshot:

`qm config {{vmid}} --snapshot {{snapname}}`
