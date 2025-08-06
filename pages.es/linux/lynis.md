# lynis

> Herramienta de seguridad y auditoría del sistema.
> Más información: <https://cisofy.com/documentation/lynis/>.

- Comprueba que Lynis está actualizado:

`sudo lynis update info`

- Realiza una auditoría del sistema:

`sudo lynis audit system`

- Realiza una auditoría de un Dockerfile:

`sudo lynis audit dockerfile {{ruta/al/dockerfile}}`
