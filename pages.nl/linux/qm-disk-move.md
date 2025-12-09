# qm disk move

> Verplaats een virtuele schijf van de ene opslag naar de andere binnen hetzelfde Proxmox cluster.
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_move>.

- Verplaats een virtuele schijf:

`qm {{[di|disk]}} {{[m|move]}} {{vm_id}} {{bestemming}} {{index}}`

- Verwijder de vorige kopie van de virtuele schijf:

`qm {{[di|disk]}} {{[m|move]}} --delete {{vm_id}} {{bestemming}} {{index}}`
