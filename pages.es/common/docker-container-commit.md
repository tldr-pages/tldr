# docker container commit

> Crea una nueva imagen a partir de los cambios de un contenedor.
> Más información: <https://docs.docker.com/reference/cli/docker/container/commit/>.

- Crea una imagen a partir de un contenedor específico:

`docker {{[commit|container commit]}} {{contenedor}} {{imagen}}:{{etiqueta}}`

- Aplica una instrucción Dockerfile `CMD` a la imagen creada:

`docker {{[commit|container commit]}} {{[-c|--change]}} "CMD {{comando}}" {{contenedor}} {{imagen}}:{{etiqueta}}`

- Aplica una instrucción `ENV` Dockerfile a la imagen creada:

`docker {{[commit|container commit]}} {{[-c|--change]}} "ENV {{nombre}}={{valor}}" {{contenedor}} {{imagen}}:{{etiqueta}}`

- Crea una imagen con un autor específico en los metadatos:

`docker {{[commit|container commit]}} {{[-a|--author]}} "{{autor}}" {{contenedor}} {{imagen}}:{{etiqueta}}`

- Crea una imagen con un comentario específico en los metadatos:

`docker {{[commit|container commit]}} {{[-m|--message]}} "{{comentario}}" {{contenedor}} {{imagen}}:{{etiqueta}}`

- Crea una imagen sin pausar el contenedor durante la confirmación:

`docker {{[commit|container commit]}} {{[-p|--pause]}} false {{contenedor}} {{imagen}}:{{etiqueta}}`

- Muestra la ayuda:

`docker {{[commit|container commit]}} --help`
