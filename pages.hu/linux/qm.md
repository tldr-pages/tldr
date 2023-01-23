# qm

> QEMU/KVM Virtual Machine Manager. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Az összes virtuális gép listázása:

`qm list`

- A helyi tárolóra feltöltött ISO-fájl segítségével hozzon létre egy virtuális gépet 4 GB-os IDE-lemezzel a `local-lvm` tárolón, 100-as azonosítóval:

`qm create {{100}} -ide0 {{local-lvm:4}} -net0 {{e1000}} -cdrom {{local:iso/proxmox-mailgateway_2.1.iso}}`

- Mutassa meg a virtuális gép konfigurációját, megadva annak azonosítóját:

`qm config {{100}}`

- Egy adott virtuális gép indítása:

`qm start {{100}}`

- Küldjön leállítási kérelmet, majd várjon, amíg a virtuális gép leáll:

`qm shutdown {{100}} && qm wait {{100}}`

- Egy virtuális gép megsemmisítése és az összes kapcsolódó erőforrás eltávolítása:

`qm destroy {{100}} --purge`
