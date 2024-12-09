# qm cleanup

> Limpia recursos en el Administrador de máquinas virtuales QEMU/KVM como dispositivos tap, VGPUs, etc.
> Llamado después de que una VM se apaga, se rompe, etc.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Limpia los recursos:

`qm cleanup {{vm_id}} {{clean-shutdown}} {{guest-requested}}`
