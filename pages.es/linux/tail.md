# tail

> Muestra las ultimas líneas de un archivo de texto
> Más información: <https://www.linuxfoundation.org/blog/blog/classic-sysadmin-14-tail-and-head-commands-in-linux-unix>.

- Mostrar las últimas 10 líneas de un archivo:

`tail /ruta/al/archivo`

- Muestra las ultimas 20 lineas de un archivo:

`tail -n 20 /ruta/al/archivo`

- Mostrar las últimas líneas de un archivo en tiempo real (seguimiento de archivos):

`tail -f /ruta/al/archivo`

Mostrar las últimas líneas de múltiples archivos:

`tail -n 5 /ruta/al/archivo1 /ruta/al/archivo2`
