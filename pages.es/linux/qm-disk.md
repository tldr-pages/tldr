# qm disk

> Administra imágenes de disco.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_import>.

- Añade `n` gigabytes a un disco virtual:

`qm {{[di|disk]}} {{[resi|resize]}} {{vm_id}} {{disk_name}} +{{n}}G`

- Mueve un disco virtual:

`qm {{[di|disk]}} {{[m|move]}} {{vm_id}} {{destino}} {{índice}}`

- Elimina la copia anterior del disco virtual:

`qm {{[di|disk]}} {{[m|move]}} --delete {{vm_id}} {{destino}} {{índice}}`

- Importa una imagen de disco VMDK/`.qcow2`/raw utilizando un nombre de almacenamiento específico:

`qm {{[di|disk]}} {{[i|import]}} {{vm_id}} {{ruta/al/disco}}{{nombre_almacenamiento}} --format {{qcow2|raw|vmdk}}`

- Vuelve a escanear todos los almacenamientos y actualiza los tamaños de disco y las imágenes de disco no utilizadas:

`qm {{[di|disk]}} {{[resc|rescan]}}`

- Realiza una simulación de un nuevo escaneo y no escribe ningún cambio en las configuraciones:

`qm {{[di|disk]}} {{[resc|rescan]}} --dryrun`

- Especifica una máquina virtual por su ID:

`qm {{[di|disk]}} {{[resc|rescan]}} --vmid {{100}}`
