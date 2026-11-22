# apt-mark

> Herramienta para cambiar el estado de los paquetes instalados.
> Más información: <https://manned.org/apt-mark>.

- Marca un paquete como instalado automáticamente:

`sudo apt-mark auto {{paquete}}`

- Mantiene un paquete en su versión actual y evita que se actualice:

`sudo apt-mark hold {{paquete}}`

- Permite que un paquete pueda ser actualizado de nuevo:

`sudo apt-mark unhold {{paquete}}`

- Muestra los paquetes instalados manualmente:

`apt-mark showmanual`

- Muestra los paquetes mantenidos que no son actualizados:

`apt-mark showhold`
