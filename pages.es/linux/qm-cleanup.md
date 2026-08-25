# qm cleanup

> Limpia los recursos del gestor de máquinas virtuales QEMU/KVM, como dispositivos tap, VGPU, etc.
> Se ejecuta después de que una máquina virtual se apaga, se colapsa, etc.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_cleanup>.

- Limpia recursos:

`qm {{[cl|cleanup]}} {{100}} {{clean-shutdown}} {{guest-requested}}`
