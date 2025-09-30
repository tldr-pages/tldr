# qm start

> Inicia una máquina virtual en el administrador de máquinas virtuales QEMU/KVM.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Inicia una máquina virtual específica:

`qm start {{100}}`

- Especifica el tipo de máquina QEMU (es decir, la CPU a emular):

`qm start {{100}} --machine {{q35}}`

- Comienza una máquina virtual específica con un tiempo de espera máximo de 60 segundos:

`qm start {{100}} --timeout {{60}}`
