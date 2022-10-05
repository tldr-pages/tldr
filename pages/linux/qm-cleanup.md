# qm cleanup 
- <vmid> <clean-shutdown> <guest-requested>

> Cleans up resources like tap devices, vgpus, etc. Called after a vm shuts down, crashes, etc.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- The (unique) ID of the VM: 
- vmid: --integer (1 - N)

- Example:
`qm cleanup {{100}}`

- Indicates if qemu shutdown cleanly:
- clean-shutdown: --boolean

- Example:
`qm cleanup --clean-shutdown:{{True}}`

- Indicates if the shutdown was requested by the guest or via qmp:
- guest-requested: --boolean

- Example:
`qm cleanup --guest-requested:{{True}}`



