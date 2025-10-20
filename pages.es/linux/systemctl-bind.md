# systemctl bind

> Monta temporalmente un archivo o directorio del host en el espacio de nombres de montaje de una unidad.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#%0A%20%20%20%20%20%20%20%20%20%20%20%20bind%0A%20%20%20%20%20%20%20%20%20%20%20%20UNIT%0A%20%20%20%20%20%20%20%20%20%20%20%20PATH%0A%20%20%20%20%20%20%20%20%20%20%20%20%5BPATH%5D%0A%20%20%20%20%20%20%20%20%20%20>.

- Monta una ruta del host en la misma ubicación dentro de la unidad:

`systemctl bind {{unidad}} /{{ruta/al/directorio_host}}`

- Monta una ruta del host en una ubicación diferente dentro de la unidad:

`systemctl bind {{unidad}} /{{ruta/al/directorio_host}} /{{ruta/al/directorio_unidad}}`

- Monta una ruta como solo lectura dentro de la unidad:

`systemctl bind {{unidad}} /{{ruta/al/directorio_host}} --read-only`

- Crea la ruta de destino dentro de la unidad antes de montar:

`systemctl bind {{unidad}} /{{ruta/al/directorio_host}} /{{ruta/al/directorio_unidad}} --mkdir`
