# docker system

> Gestiona datos de Docker y muestra información del sistema.
> Más información: <https://docs.docker.com/reference/cli/docker/system/>.

- Muestra el uso de disco de Docker:

`docker system df`

- Muestra información detallada sobre el uso de disco:

`docker system df {{[-v|--verbose]}}`

- Elimina datos no utilizados (agrega `--volumes` para eliminar también los volúmenes no utilizados):

`docker system prune`

- Elimina datos no utilizados creados hace más del tiempo especificado:

`docker system prune --filter "until={{horas}}h{{minutos}}m"`

- Muestra eventos en tiempo real del daemon de Docker:

`docker system events`
