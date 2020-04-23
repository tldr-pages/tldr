# apt-mark

> Herramienta para cambiar el estado de los paquetes instalados.

- Marca un paquete como instalado automáticamente:

`sudo apt-mark auto {{nombre_paquete}}`

- Mantiene un paquete en su versión actual y evita que se actualice:

`sudo apt-mark hold {{nombre_paquete}}`

- Permite que un paquete pueda ser actualizado de nuevo:

`sudo apt-mark unhold {{nombre_paquete}}`

- Muestra los paquetes instalados manualmente:

`apt-mark showmanual`

- Muestra los paquetes mantenidos que no son actualizados:

`apt-mark showhold`
