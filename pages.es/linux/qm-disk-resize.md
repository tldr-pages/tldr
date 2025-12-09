# qm disk resize

> Redimensiona un disco de máquina virtual en el entorno virtual Proxmox (PVE).
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_resize>.

- Añade `n` gigabytes a un disco virtual:

`qm disk resize {{vm_id}} {{nombre_de_disco}} +{{n}}G`
