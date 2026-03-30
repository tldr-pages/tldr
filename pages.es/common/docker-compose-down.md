# docker compose down

> Detiene y elimina los contenedores, redes, imágenes y volúmenes creados por `docker compose up`.
> Más información: <https://docs.docker.com/reference/cli/docker/compose/down/>.

- Detiene y elimina todos los contenedores y redes:

`docker compose down`

- Detiene y elimina contenedores, redes y todas las imágenes usadas por los servicios:

`docker compose down --rmi all`

- Detiene y elimina contenedores, redes y solo las imágenes sin etiqueta personalizada:

`docker compose down --rmi local`

- Detiene y elimina contenedores, redes y todos los volúmenes:

`docker compose down {{[-v|--volumes]}}`

- Detiene y elimina todo incluyendo contenedores huérfanos:

`docker compose down --remove-orphans`

- Detiene y elimina contenedores usando un archivo compose alternativo:

`docker compose {{[-f|--file]}} {{ruta/a/config}} down`

- Detiene y elimina contenedores con un tiempo de espera personalizado en segundos:

`docker compose down {{[-t|--timeout]}} {{tiempo_espera}}`
