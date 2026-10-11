# podman commit

> Crea una nueva imagen basada en el contenedor modificado.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-commit.1.html>.

- Crea una imagen a partir de un contenedor específico:

`podman commit {{contenedor}} {{imagen}}:{{etiqueta}}`

- Aplica una instrucción `ENV` a la imagen creada:

`podman commit {{[-c|--change]}} "ENV {{nombre}}={{valor}}" {{contenedor}} {{imagen}}:{{etiqueta}}`

- Aplicar las instrucciones `LABEL`, `ENTRYPOINT` y `CMD` a la imagen creada:

`podman commit {{[-c|--change]}} CMD={{comando}} {{[-c|--change]}} ENTRYPOINT={{comando}} {{[-c|--change]}} "LABEL {{clave}}={{valor}}" {{contenedor}} {{imagen}}:{{etiqueta}}`

- Crea una imagen con un autor y un comentario específicos en los metadatos:

`podman commit {{[-a|--author]}} "{{autor}}" {{[-m|--message]}} "{{comentario}}" {{contenedor}} {{imagen}}:{{etiqueta}}`

- Crea una imagen sin pausar el contenedor durante la confirmación:

`podman commit {{[-p|--pause]}} false {{contenedor}} {{imagen}}:{{etiqueta}}`

- Muestra la ayuda:

`podman commit --help`
