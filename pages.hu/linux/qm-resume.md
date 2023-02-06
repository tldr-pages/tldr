# qm resume

> Virtuális gép folytatása. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Egy adott virtuális gép folytatása:

`qm resume {{vm_id}}`

- Egy adott virtuális gép folytatása a zárolások figyelmen kívül hagyásával (root hozzáférést igényel):

`sudo qm resume {{vm_id}} --skiplock true`
