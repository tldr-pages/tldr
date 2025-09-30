# qm

> Administrador de máquinas virtuales QEMU/KVM.
> Algunas órdenes como `list`, `start`, `stop`, `clone`, etc. tienen su propia documentación.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Lista todas las máquinas virtuales:

`qm list`

- Dado un archivo ISO subido en el almacenamiento local, crea una máquina virtual con un disco IDE de 4 GB en el almacenamiento `local-lvm` y con ID 100:

`qm create {{100}} -ide0 {{local-lvm:4}} -net0 {{e1000}} -cdrom {{local:iso/proxmox-mailgateway_2.1.iso}}`

- Muestra la configuración de una máquina virtual especificando su ID:

`qm config {{100}}`

- Inicia una máquina virtual específica:

`qm start {{100}}`

- Envía una solicitud de apagado, luego espera hasta que se detenga la máquina virtual:

`qm shutdown {{100}} && qm wait {{100}}`

- Destruye una máquina virtual y elimina todos los recursos relacionados:

`qm destroy {{100}} --purge`
