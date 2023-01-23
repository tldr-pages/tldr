# qm clone

> A virtuális gép másolatának létrehozása a QEMU/KVM Virtual Machine Managerben. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Virtuális gép másolása:

`qm copy {{vm_id}} {{new_vm_id}}`

- Virtuális gép másolása egy adott név használatával:

`qm copy {{vm_id}} {{new_vm_id}} --name {{name}}`

- Virtuális gép másolása egy adott leírásn keresztül:

`qm copy {{vm_id}} {{new_vm_id}} --description {{description}}`

- Virtuális gép másolása az összes lemez teljes másolatának létrehozása:

`qm copy {{vm_id}} {{new_vm_id}} --full`

- Virtuális gép másolása egy adott fájltárolási formátumot használva ( `--full`):

`qm copy {{vm_id}} {{new_vm_id}} --full --format {{qcow2|raw|vmdk}}`

- Egy virtuális gép másolása, majd hozzáadása egy adott poolhoz:

`qm copy {{vm_id}} {{new_vm_id}} --pool {{pool_name}}`
