# qm disk import

> Importa una imagen de disco a una máquina virtual como un disco sin utilizar.
> Los formatos de imagen que `qemu-img` soporta son: raw, qcow2, qed, vdi, vmdk, y vhd.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Importa una imagen de disco VMDK/qcow2/raw usando un nombre de almacenamiento específico:

`qm disk import {{vm_id}} {{ruta/al/disco}} {{nombre_del_disco}} --format {{qcow2|raw|vmdk}}`
