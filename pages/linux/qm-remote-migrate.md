# qm remote-migrate

> Migrate a virtual machine to a remote Proxmox host or cluster.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_remote-migrate>.

- Migrate a VM to a remote host:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge {{bridge}} --target-storage {{storage}}`

- Migrate a running VM with live migration:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge {{bridge}} --target-storage {{storage}} --online`

- Delete the source VM after a successful migration:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge {{bridge}} --target-storage {{storage}} --delete 1`

- Limit migration bandwidth:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge {{bridge}} --target-storage {{storage}} --bwlimit {{value}}`

- Use the same bridge and storage names on the target:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge 1 --target-storage 1`

- Connect to a remote API on a custom port:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}},port={{porta}}' --target-bridge {{bridge}} --target-storage {{storage}}`
