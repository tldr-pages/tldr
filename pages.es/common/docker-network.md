# docker network

> Crea y gestiona redes de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/network/>.

- Lista todas las redes disponibles y configuradas en el daemon de Docker:

`docker network ls`

- Crea una red definida por el usuario:

`docker network create {{[-d|--driver]}} {{nombre_driver}} {{nombre_red}}`

- Muestra información detallada sobre una o más redes:

`docker network inspect {{nombre_red1 nombre_red2 ...}}`

- Conecta un contenedor a una red usando un nombre o ID:

`docker network connect {{nombre_red}} {{nombre_contenedor|ID}}`

- Desconecta un contenedor de una red:

`docker network disconnect {{nombre_red}} {{nombre_contenedor|ID}}`
