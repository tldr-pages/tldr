# nix classic

> Una interfaz clásica y estable para un potente gestor de paquetes que hace la gestión de paquetes fiable, reproducible y declarativa.
> Algunos comandos Nix como `nix-build`, `nix-shell`, `nix-env`, y `nix-store` tienen sus propias páginas. Ver también: `tldr nix`.
> Más información: <https://nixos.org>.

- Busca un paquete en nixpkgs a través de su nombre:

`nix-env -qaP {{termino_busqueda_regexp}}`

- Inicia un shell con los paquetes especificados disponibles:

`nix-shell -p {{pkg1 pkg2 pkg3...}}`

- Instala algunos paquetes de forma permanente:

`nix-env -iA {{nixpkgs.pkg1 nixpkgs.pkg2...}}`

- Muestra todas las dependencias de una ruta de almacenamiento (paquete), en formato de árbol:

`nix-store --query --tree {{/nix/store/...}}`

- Actualiza los canales (repositorios):

`nix-channel --update`

- Elimina rutas no utilizadas del almacén Nix:

`nix-collect-garbage`
