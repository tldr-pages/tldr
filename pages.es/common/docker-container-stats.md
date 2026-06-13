# docker container stats

> Muestra una transmisión en vivo de las estadísticas de uso de recursos de los contenedores.
> Más información: <https://docs.docker.com/reference/cli/docker/container/stats/>.

- Muestra una transmisión en vivo de las estadísticas de todos los contenedores en ejecución:

`docker {{[stats|container stats]}}`

- Muestra una transmisión en vivo de las estadísticas de uno o más contenedores:

`docker {{[stats|container stats]}} {{contenedor1 contenedor2 ...}}`

- Cambia el formato de las columnas para mostrar el porcentaje de uso de la CPU del contenedor:

`docker {{[stats|container stats]}} --format "{{.Name}}:\t{{.CPUPerc}}"`

- Muestra estadísticas de todos los contenedores (tanto en ejecución como detenidos):

`docker {{[stats|container stats]}} {{[-a|--all]}}`

- Desactiva las estadísticas en tiempo real y solo extrae las estadísticas actuales:

`docker {{[stats|container stats]}} --no-stream`
