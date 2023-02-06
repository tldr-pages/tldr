# qm stop

> Virtuális gép leállítása. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Virtuális gép azonnali leállítása:

`qm stop {{VM_ID}}`

- Állítson le egy virtuális gépet, és várjon legfeljebb 10 másodpercet:

`qm stop --timeout {{10}} {{VM_ID}}`

- Egy virtuális gép leállítása és a zárolás kihagyása (ezt az opciót csak a rendszergazda használhatja):

`qm stop --skiplock {{true}} {{VM_ID}}`

- Leállítani egy virtuális gépet, és nem deaktiválni a tároló köteteket:

`qm stop --keepActive {{true}} {{VM_ID}}`
