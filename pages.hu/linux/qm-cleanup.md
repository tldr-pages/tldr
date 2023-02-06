# qm cleanup

> A QEMU/KVM virtuális gépkezelő erőforrásainak, például a csapeszközöknek, VGPU-knak, stb. a megtisztítása.A VM leállítása, összeomlása, stb. után hívódik. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Erőforrások tisztítása:

`qm cleanup {{vm_id}} {{clean-shutdown}} {{guest-requested}}`
