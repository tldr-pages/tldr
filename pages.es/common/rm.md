# rm

> Eliminar archivos o directorios.

- Elimina archivos de ubicaciones arbitrarias:

`rm {{ruta/hacia/archivo}} {{ruta/hacia/otro/archivo}}`

- Elimina, de forma recursiva, un directorio y todos sus subdirectorios:

`rm -r {{ruta/hacia/directorio}}`

- Elimina un directorio a la fuerza, sin pedir confirmación ni mostrar mensajes de error:

`rm -rf {{ruta/hacia/directorio}}`

- Elimina varios archivos de forma interactiva, solicitando confirmación antes de eliminar cada archivo:

`rm -i {{archivo(s)}}`

- Elimina archivos en modo detallado, imprimiendo un mensaje por cada archivo eliminado:

`rm -v {{ruta/hacia/directorio/*}}`
