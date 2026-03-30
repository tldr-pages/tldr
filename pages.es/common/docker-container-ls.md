# docker container ls

> Lista los contenedores de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Lista los contenedores de Docker en ejecución:

`docker {{[ps|container ls]}}`

- Lista todos los contenedores de Docker (en ejecución y detenidos):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Muestra el último contenedor creado (incluye todos los estados):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Filtra contenedores que contienen una subcadena en su nombre:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{nombre}}"`

- Filtra contenedores que comparten una imagen como ancestro:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{imagen}}:{{etiqueta}}"`

- Filtra contenedores por código de estado de salida:

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{código}}"`

- Filtra contenedores por estado (created, running, removing, paused, exited, dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{estado}}"`
