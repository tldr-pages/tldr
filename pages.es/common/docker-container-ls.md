# docker container ls

> Muestra una lista de contenedores de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Muestra los contenedores de Docker que se están ejecutando actualmente:

`docker {{[ps|container ls]}}`

- Muestra todos los contenedores Docker (en ejecución y detenidos):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Muestra el contenedor creado más recientemente (incluye todos los estados):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Filtra contenedores que contienen una subcadena en su nombre:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{nombre}}"`

- Filtra contenedores que compartan una imagen determinada como antecesora:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Filtra contenedores por código de estado de salida:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "exited={{codigo}}" {{[-a|--all]}}`

- Filtra contenedores por estado (creado, en ejecución, en eliminación, en pausa, cerrado o inactivo):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{estado}}"`

- Filtra contenedores que montan un volumen específico o tienen un volumen montado en una ruta específica:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{ruta/a/directorio}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
