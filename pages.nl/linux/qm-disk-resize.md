# qm disk resize

> Wijzig de grote van een virtuele machine schijf in the Proxmox Virtual Environment (PVE).
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_resize>.

- Voeg `n` gigabytes toe aan een virtuele schijf:

`qm {{[di|disk]}} {{[resi|resize]}} {{vm_id}} {{schijfnaam}} +{{n}}G`
