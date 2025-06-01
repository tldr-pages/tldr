# nix-env

> Manipula o consulta entornos de usuario de Nix.
> Más información: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- Lista todos los paquetes instalados:

`nix-env {{[-q|--query]}}`

- Consulta los paquetes instalados:

`nix-env {{[-q|--query]}} {{término_de_búsqueda}}`

- Consulta los paquetes disponibles:

`nix-env {{[-qa|--query --available]}} {{término_de_búsqueda}}`

- Instala un paquete:

`nix-env {{[-iA|--install --attr]}} nixpkgs.{{nombre_del_paquete}}`

- Instala un paquete desde un enlace:

`nix-env {{[-i|--install]}} {{nombre_del_paquete}} {{[-f|--file]}} {{example.com}}`

- Desinstala un paquete:

`nix-env {{[-e|--uninstall]}} {{nombre_del_paquete}}`

- Actualiza un paquete:

`nix-env {{[-u|--upgrade]}} {{nombre_del_paquete}}`

- Actualiza todos los paquetes:

`nix-env {{[-u|--upgrade]}}`
