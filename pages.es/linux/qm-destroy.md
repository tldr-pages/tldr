# qm destroy

> Destruye una máquina virtual del administrador de máquinas virtuales EMU/KVM.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_destroy>.

- Destruye una máquina virtual específica:

`qm destroy {{id_mv}}`

- Destruye todos los discos que no se mencionan explícitamente en la configuración de una máquina virtual específica:

`qm destroy {{id_mv}} --destroy-unreferenced-disks`

- Destruye una máquina virtual y la elimina de todos los lugares (inventarios, trabajos de copia de seguridad, manejadores de alta disponibilidad, etc.):

`qm destroy {{id_mv}} --purge`

- Destruye una máquina virtual específica ignorando las cerraduras (locks) y forzando su destrucción:

`sudo qm destroy {{id_mv}} --skiplock`
