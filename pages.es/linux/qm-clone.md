# qm clone

> Crea una copia de la máquina virtual en el Administrador de Máquinas Virtuales QEMU/KVM.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Copia una máquina virtual:

`qm copy {{id_mv}} {{id_nueva_mv}}`

- Copia una máquina virtual usando un nombre específico:

`qm copy {{id_mv}} {{id_nueva_mv}} --name {{nombre}}`

- Copia una máquina virtual usando una descripción específica:

`qm copy {{id_mv}} {{id_nueva_mv}} --description {{descripción}}`

- Copia una máquina virtual creando una copia completa de todos los discos:

`qm copy {{id_mv}} {{id_nueva_mv}} --full`

- Copia una máquina virtual usando un formato específico para el almacenamiento de archivos (requiere `--full`):

`qm copy {{id_mv}} {{id_nueva_mv}} --full --format {{qcow2|raw|vmdk}}`

- Copia una máquina virtual y luego la añade a un grupo (pool) específico:

`qm copy {{id_mv}} {{id_nueva_mv}} --pool {{nombre_grupo}}`
