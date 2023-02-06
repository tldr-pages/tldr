# qm wait

> Várjon, amíg a virtuális gép leáll. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Várjon, amíg a virtuális gép leáll:

`qm wait {{vm_id}}`

- Várjon, amíg a virtuális gép 10 másodperces időkorlátozással leáll:

`qm wait --timeout {{10}} {{vm_id}}`

- Küldjön leállítási kérelmet, majd várjon, amíg a virtuális gép 10 másodperces időkorlátozással leáll:

`qm shutdown {{vm_id}} && qm wait --timeout {{10}} {{vm_id}}`
