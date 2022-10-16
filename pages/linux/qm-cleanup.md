# qm cleanup

> Cleans up resources like tap devices, vgpus, etc. Called after a vm shuts down, crashes, etc.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Clean up resources like tap devices, vgpus, etc. after vm shuts down, crashes, etc:

`qm cleanup {{vmid}} {{clean-shutdown}} {{guest-requested}}`
