# limactl

> Administrador de máquinas virtuales para huéspedes Linux, con múltiples plantillas para MV (Máquinas virtuales) disponibles.
> Se puede utilizar para ejecutar contenedores en macOS, pero también para casos de uso genéricos de máquinas virtuales en anfitriones macOS y Linux.
> Más información: <https://github.com/lima-vm/lima>.

- Lista MVs (Máquinas virtuales):

`limactl list`

- Crea una MV usando la configuración predeterminada y opcionalmente proporciona un nombre y/o una plantilla (vea `limactl create --list-templates` para plantillas disponibles):

`limactl create --name {{nombre_de_la_mv}} template://{{debian|fedora|ubuntu|...}}`

- Inicia una MV (esto puede instalar algunas dependencias en la misma y tomar unos minutos):

`limactl start {{nombre_de_la_mv}}`

- Abre un intérprete de comandos dentro de una MV:

`limactl shell {{nombre_de_la_mv}}`

- Ejecuta un comando dentro de una MV:

`limactl shell {{nombre_de_la_mv}} {{comando}}`

- Detiene/apaga una MV:

`limactl stop {{nombre_de_la_mv}}`

- Suprime una MV:

`limactl remove {{nombre_de_la_mv}}`
