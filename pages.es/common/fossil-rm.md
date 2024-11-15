# fossil rm

> Elimina archivos o directorios del control de versiones Fossil.
> Vea también: `fossil forget`.
> Más información: <https://fossil-scm.org/home/help/rm>.

- Elimina un archivo o directorio del control de versiones Fossil:

`fossil rm {{ruta/al/archivo_o_directorio}}`

- Elimina un archivo o directorio del control de versiones Fossil, y también lo elimina del disco:

`fossil rm --hard {{ruta/al/archivo_o_directorio}}`

- Añade nuevamente todos los archivos previamente eliminados y no comprometidos (uncommitted) al control de versiones Fossil:

`fossil rm --reset`
