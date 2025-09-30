# choco uninstall

> Desinstala paquetes con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-uninstall>.

- Desinstalar uno o más paquetes:

`choco uninstall {{paquete1 paquete2 ...}}`

- Desinstalar una versión específica de un paquete:

`choco uninstall {{paquete}} --version {{versión}}`

- Confirmar automáticamente todos los mensajes:

`choco uninstall {{paquete}} --yes`

- Eliminar todas las dependencias al desinstalar:

`choco uninstall {{paquete}} --remove-dependencies`

- Desinstalar todos los paquetes:

`choco uninstall all`
