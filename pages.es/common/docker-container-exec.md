# docker container exec

> Ejecuta un comando en un contenedor Docker que ya se está ejecutando.
> Más información: <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Abre una sesión de intérprete de comandos interactiva en un contenedor que ya está funcionando:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{nombre_contenedor}} {{/bin/bash}}`

- Ejecuta un comando en segundo plano (desconectado) en un contenedor en ejecución:

`docker {{[exec|container exec]}} {{[-d|--detach]}} {{nombre_contenedor}} {{comando}}`

- Seleccionar el directorio de trabajo para ejecutar un comando determinado:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{ruta/al/directorio}} {{nombre_del_contenedor}} {{comando}}`

- Ejecutar un comando en segundo plano en un contenedor existente, pero mantener `stdin` abierto:

`docker {{[exec|container exec]}} {{[-i|--interactive]}} {{[-d|--detach]}} {{nombre_contenedor}} {{comando}}`

- Establece una variable de entorno en una sesión Bash en ejecución:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-e|--env]}} {{nombre_variable}}={{valor}} {{nombre_contenedor}} {{/bin/bash}}`

- Ejecuta un comando como un usuario específico:

`docker {{[exec|container exec]}} {{[-u|--user]}} {{usuario}} {{nombre_contenedor}} {{comando}}`
