# qm shutdown

> Virtuális gép leállítása a QEMU/KVM Virtual Machine Managerben. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Virtuális gép leállítása:

`qm shutdown {{VM_ID}}`

- A virtuális gép leállítása legfeljebb 10 másodperces várakozás után:

`qm shutdown --timeout {{10}} {{VM_ID}}`

- A virtuális gép leállítása és a tároló kötetek deaktiválása nélkül:

`qm shutdown --keepActive {{true}} {{VM_ID}}`

- Virtuális gép leállítása és a zárolás kihagyása (ezt az opciót csak a rendszergazda használhatja):

`qm shutdown --skiplock {{true}} {{VM_ID}}`

- Virtuális gép leállítása és leállítása:

`qm shutdown --forceStop {{true}} {{VM_ID}}`
