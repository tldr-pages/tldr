# nixos-rebuild

> Reconfigura una máquina de NixOS.
> Más información: <https://nixos.org/nixos/manual/#sec-changing-config>.

- Construye y cambia a la configuración nueva, haciéndola la predeterminada al arrancar el sistema:

`sudo nixos-rebuild switch`

- Construye y cambia a la configuración nueva, haciéndola la predeterminada al arrancar el sistema (con un nombre):

`sudo nixos-rebuild switch {{[-p|--profile-name]}} {{nombre}}`

- Construye y cambia a la configuración nueva, haciéndola la predeterminada al arrancar el sistema e instalando actualizaciones:

`sudo nixos-rebuild switch --upgrade`

- Revierte cambios a la configuración, cambiando a la generación previa:

`sudo nixos-rebuild switch --rollback`

- Construye la configuración nueva y la predetermina sin cambiar a ella:

`sudo nixos-rebuild boot`

- Construye y activa la configuración nueva, pero no la haga la entrada de arranque predeterminada (solo para finalidad de pruebas):

`sudo nixos-rebuild test`

- Construye la configuración nueva y la abre en un hipervisor:

`sudo nixos-rebuild build-vm`

- Lista generaciones disponibles similarmente al menú del cargador de arranque:

`nixos-rebuild list-generations`
