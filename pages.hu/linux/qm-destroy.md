# qm destroy

> Virtuális gép megsemmisítése a QEMU/KVM Virtual Machine Managerben. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Egy adott virtuális gép megsemmisítése:

`qm destroy {{vm_id}}`

- Az összes olyan lemez megsemmisítése, amelyre nem hivatkozik kifejezetten egy adott virtuális gép konfigurációja:

`qm destroy {{vm_id}} --destroy-unreferenced-disks`

- Egy virtuális gép megsemmisítése és eltávolítása minden helyről (leltár, biztonsági mentési feladatok, magas rendelkezésre állású menedzserek stb.):

`qm destroy {{vm_id}} --purge`

- Egy adott virtuális gép megsemmisítése a zárolások figyelmen kívül hagyásával és a megsemmisítés kikényszerítésével:

`sudo qm destroy {{vm_id}} --skiplock`
