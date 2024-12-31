# qmrestore

> Restaura copias de seguridad de QemuServer `vzdump`.
> Más información: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Restaura la máquina virtual desde un archivo de respaldo dado en el almacenamiento original:

`qmrestore {{ruta/a/vzdump-qemu-100.vma.lzo}} {{100}}`

- Sobrescribe la máquina virtual existente desde un archivo de respaldo dado en el almacenamiento original:

`qmrestore {{ruta/a/vzdump-qemu-100.vma.lzo}} {{100}} --force true`

- Restaura la máquina virtual de un archivo de respaldo dado en el almacenamiento específico:

`qmrestore {{ruta/a/vzdump-qemu-100.vma.lzo}} {{100}} --storage {{local}}`

- Inicia la máquina virtual de inmediato desde la copia de seguridad mientras se restaura en el fondo (background) (sólo en el servidor de respaldo Proxmox):

`qmrestore {{ruta/a/vzdump-qemu-100.vma.lzo}} {{100}} --live-restore true`
