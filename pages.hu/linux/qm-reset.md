# qm reset

> Virtuális gép visszaállítása a QEMU/KVM Virtual Machine Managerben. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Virtuális gép visszaállítása:

`qm reset {{vm_id}}`

- Virtuális gép visszaállítása és a zárolás kihagyása (ezt az opciót csak a rendszergazda használhatja):

`qm reset --skiplock {{true}} {{vm_id}}`
