# docker search

> Busca imágenes de Docker en Docker Hub.
> Más información: <https://docs.docker.com/reference/cli/docker/search/>.

- Busca imágenes de Docker por nombre o palabra clave:

`docker search {{palabra_clave}}`

- Busca imágenes y muestra solo las oficiales:

`docker search {{[-f|--filter]}} is-official=true {{palabra_clave}}`

- Busca imágenes y muestra solo las compilaciones automatizadas:

`docker search {{[-f|--filter]}} is-automated=true {{palabra_clave}}`

- Busca imágenes con un número mínimo de estrellas:

`docker search {{[-f|--filter]}} stars={{número}} {{palabra_clave}}`

- Limita el número de resultados:

`docker search --limit {{número}} {{palabra_clave}}`

- Personaliza el formato de salida:

`docker search {{[-f|--format]}} "{{.Name}}: {{.Description}}" {{palabra_clave}}`
