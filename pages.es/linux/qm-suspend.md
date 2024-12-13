# qm suspend

> Suspende una máquina virtual (MV) en el entorno virtual Proxmox (PVE).
> Usa las banderas de `--skiplock` y `--skiplockstorage` con precaución, ya que pueden conducir a la corrupción de datos en ciertas situaciones.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Suspende una máquina virtual por ID:

`qm suspend {{id_mv}} {{entero}}`

- Omite el chequeo de bloqueo al suspender una MV:

`qm suspend {{id_mv}} {{entero}} --skiplock`

- Omite el chequeo de bloqueo por almacenamiento al suspender una MV:

`qm suspend {{id_mv}} {{entero}} --skiplockstorage`
