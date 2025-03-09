# rm

> Elimina archivos o directorios.
> Vea también: `rmdir`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Elimina archivos específicos:

`rm {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Elimina archivos específicos ignorando los que no existen:

`rm -f {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Elimina varios archivos de forma interactiva, solicitando confirmación antes de eliminar cada archivo:

`rm -i {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Elimina archivos, imprimiendo un mensaje por cada archivo eliminado:

`rm -v {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Elimina, de forma recursiva, archivos y directorios:

`rm -r {{ruta/al/directorio1 ruta/al/directorio2 ...}}`
