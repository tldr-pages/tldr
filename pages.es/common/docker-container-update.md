# docker container update

> Actualiza la configuración de los contenedores de Docker.
> Nota: Este comando no es compatible con contenedores de la plataforma Windows.
> Más información: <https://docs.docker.com/reference/cli/docker/container/update/>.

- Actualiza la política de reinicio para que se aplique cuando un contenedor específico se cierre:

`docker {{[update|container update]}} --restart {{always|no|on-failure|unless-stopped}} {{nombre_contenedor}}`

- Actualiza la política para reiniciar hasta tres veces un contenedor específico cuando se cierre con un estado de salida distinto de cero:

`docker {{[update|container update]}} --restart on-failure:3 {nombre_contenedor}`

- Actualiza el número de CPU disponibles para un contenedor específico:

`docker {{[update|container update]}} --cpus {{count}} {{contenedor_nombre}}`

- Actualiza el límite de memoria en [M]egabytes para un contenedor específico:

`docker {{[update|container update]}} {{[-m|--memory]}} {{limit}}M {{nombre_contenedor}}`

- Actualiza el número máximo de ID de proceso permitidos dentro de un contenedor específico (utilice `-1` para ilimitado):

`docker {{[update|container update]}} --pids-limit {{count}} {{nombre_contenedor}}`

- Actualiza la cantidad de memoria en [M]egabytes que un contenedor específico puede intercambiar al disco (utilice `-1` para ilimitado):

`docker {{[update|container update]}} --memory-swap {{limit}}M {{nombre_contenedor}}`
