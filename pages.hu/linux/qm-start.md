# qm start

> Virtuális gép indítása a QEMU/KVM Virtual Machine Manager-en. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Egy adott virtuális gép indítása:

`qm start {{100}}`

- Adja meg a QEMU gép típusát (azaz az emulálni kívánt CPU-t):

`qm start {{100}} --machine {{q35}}`

- Indítson el egy adott virtuális gépet 60 másodperces időkorlátozással:

`qm start {{100}} --timeout {{60}}`
