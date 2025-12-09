# podman machine

> Crea y gestiona máquinas virtuales ejecutando Podman.
> Desde la versión 4 o superior de Podman.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- Lista máquinas existentes:

`podman machine ls`

- Crea una nueva máquina predeterminada:

`podman machine init`

- Crea una nueva máquina con un nombre específico:

`podman machine init {{nombre}}`

- Crea una nueva máquina con diferentes recursos:

`podman machine init --cpus={{4}} --memory={{4096}} --disk-size={{50}}`

- Inicia o detiene una máquina:

`podman machine {{start|stop}} {{nombre}}`

- Conecta a una máquina en ejecución a través de SSH:

`podman machine ssh {{nombre}}`

- Inspecciona información sobre una máquina:

`podman machine inspect {{nombre}}`
