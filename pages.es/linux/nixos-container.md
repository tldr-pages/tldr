# nixos-container

> Inicia contenedores de NixOS usando contenedores de Linux.
> Más información: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- Lista contenedores activos:

`sudo nixos-container list`

- Crea un contenedor de NixOS con un archivo de configuración específico:

`sudo nixos-container create {{nombre_del_contenedor}} --config-file {{ruta_a_la_configuracion_de_nix}}`

- Inicia, detiene, termina o destruye un contenedor específico:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{nombre_del_contenedor}}`

- Ejecuta un comando dentro de un contenedor activo:

`sudo nixos-container run {{nombre_del_contenedor}} -- {{comando}} {{argumentos_del_comando}}`

- Actualiza la configuración de un contenedor:

`sudo $EDITOR /var/lib/container/{{nombre_del_contenedor}}/etc/nixos/configuration.nix && sudo nixos-container update {{nombre_del_contenedor}}`

- Entra a una sesión de shell interactivo en un contenedor que ya está activo:

`sudo nixos-container root-login {{nombre_del_contenedor}}`
