# rm

> Elimina archivos o directorios.

- Elimina archivos de ubicaciones arbitrarias:

`rm {{ruta/al/archivo}} {{ruta/al/otro/archivo}}`

- Elimina, de forma recursiva, un directorio y todos sus subdirectorios:

`rm -r {{ruta/al/directorio}}`

- Elimina un directorio a la fuerza, sin pedir confirmación ni mostrar mensajes de error:

`rm -rf {{ruta/al/directorio}}`

- Elimina varios archivos de forma interactiva, solicitando confirmación antes de eliminar cada archivo:

`rm -i {{archivo(s)}}`

- Elimina archivos en modo detallado, imprimiendo un mensaje por cada archivo eliminado:

`rm -v {{ruta/hacia/directorio/*}}`
