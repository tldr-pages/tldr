# qm start

> Démarre une machine virtuelle avec QEMU/KVM Virtual Machine Manager.
> Plus d'informations : <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_start>.

- Démarre une machine virtuelle spécifique :

`qm start {{100}}`

- Spécifie le type de machine QEMU (c'est-à-dire le processeur à émuler) :

`qm start {{100}} --machine {{q35}}`

- Démarre une machine virtuelle spécifique avec un délai d'attente de 60 secondes :

`qm start {{100}} --timeout {{60}}`
