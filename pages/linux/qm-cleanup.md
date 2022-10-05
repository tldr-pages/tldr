# qm cleanup 

> Cleans up resources like tap devices, vgpus, etc. Called after a vm shuts down, crashes, etc.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- The (unique) ID of the VM.
`vmid: --integer {{(1 - N)}}

- Indicates if qemu shutdown cleanly.
`clean-shutdown: --boolean

-Indicates if the shutdown was requested by the guest or via qmp.
`guest-requested: --boolean

