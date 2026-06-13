# qm suspend

> Suspende una máquina virtual (MV) en el entorno virtual Proxmox (PVE).
> Usa las banderas de `--skiplock` y `--skiplockstorage` con precaución, ya que pueden conducir a la corrupción de datos en ciertas situaciones.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_suspend>.

- Suspende una máquina virtual por ID:

`qm {{[su|suspend]}} {{100}} {{entero}}`

- Omite el chequeo de bloqueo al suspender una MV:

`qm {{[su|suspend]}} {{100}} {{entero}} --skiplock`

- Omite el chequeo de bloqueo por almacenamiento al suspender una MV:

`qm {{[su|suspend]}} {{100}} {{entero}} --skiplockstorage`
