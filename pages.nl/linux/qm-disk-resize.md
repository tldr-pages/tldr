# qm disk resize

> Wijzig de grote van een virtuele machine schijf in the Proxmox Virtual Environment (PVE).
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Voeg `n` gigabytes toe aan een virtuele schijf:

`qm disk resize {{vm_id}} {{schijfnaam}} +{{n}}G`
