# fossil delete

> Elimina archivos o directorios del control de versiones Fossil.
> Vea también: `fossil forget`.
> Más información: <https://fossil-scm.org/home/help/delete>.

- Elimina un archivo o directorio del control de versiones Fossil:

`fossil {{[rm|delete]}} {{ruta/al/archivo_o_directorio}}`

- Elimina un archivo o directorio del control de versiones Fossil y también lo elimina del disco:

`fossil {{[rm|delete]}} --hard {{ruta/al/archivo_o_directorio}}`

- Añade nuevamente todos los archivos previamente eliminados y no comprometidos (uncommitted) al control de versiones Fossil:

`fossil {{[rm|delete]}} --reset`
