# podman ps

> Lista los contenedores Podman.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- Lista los contenedores Podman actualmente en ejecución:

`podman ps`

- Lista todos los contenedores Podman (corriendo y detenidos):

`podman ps --all`

- Muestra el último contenedor creado (incluye todos los estados):

`podman ps --latest`

- Filtra los contenedores que contienen una subcadena en su nombre:

`podman ps --filter "name={{nombre}}"`

- Filtra los contenedores que comparten una imagen dada como ancestro:

`podman ps --filter "ancestor={{imagen}}:{{etiqueta}}"`

- Filtra por código de estado de salida:

`podman ps --all --filter "exited={{código}}"`

- Filtra los contenedores por estado (created, running, removing, paused, exited y dead). Se usa el término en inglés:

`podman ps --filter "status={{estado}}"`

- Filtra contenedores que montan un volumen específico o tienen un volumen montado en una ruta específica:

`podman ps --filter "volume={{ruta/al/directorio}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
