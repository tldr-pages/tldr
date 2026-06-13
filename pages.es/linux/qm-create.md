# qm create

> Crea o restaura una máquina virtual en el administrador de máquinas virtuales QEMU/KVM.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_create>.

- Crea una máquina virtual:

`qm create {{100}}`

- Inicia automáticamente la máquina después de su creación:

`qm create {{100}} --start 1`

- Especifica el tipo de sistema operativo en la máquina virtual:

`qm create {{100}} --ostype {{win10}}`

- Reemplaza una máquina existente (requiere archivarla):

`qm create {{100}} --archive {{ruta/al/archivo_de_respaldo.tar}} --force 1`

- Especifica un guión (script) a ejecutar automáticamente dependiendo del estado de la máquina virtual:

`qm create {{100}} --hookscript {{ruta/al/guión.pl}}`
