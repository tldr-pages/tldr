# tail

> Muestra las ultimas líneas de un archivo de texto en especifico
> Más información: <https://www.linuxfoundation.org/blog/blog/classic-sysadmin-14-tail-and-head-commands-in-linux-unix>.

- Imprime las últimas 10 líneas de un archivo:

`tail /ruta/al/archivo`

- Imprime las ultimas 20 lineas de un archivo:

`tail --lines conteo /ruta/al/archivo`

- Imprime las últimas líneas de un archivo en tiempo real (seguimiento de archivos):

`tail --follow /ruta/al/archivo`

- Imprime las últimas líneas de un archivo y se actualiza cada 'n' segundos:

`tail --sleep-interval segundos /ruta/al/archivo`

- Imprime un numero especifico de bytes desde el final de algun archivo

`tail --bytes conteo /ruta/al/archivo`

- Imprime las ultimas lineas de un archivo aun si este es inaccesible

`tail --retry conteo /ruta/al/archivo`
