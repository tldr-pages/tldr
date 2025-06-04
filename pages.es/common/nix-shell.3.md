# nix shell

> Inicia un shell en lo cual los paquetes especificados están disponibles.
> Vea también: `nix-shell` para armar un entorno de desarrollo, `nix flake` para información sobre los flakes.
> Más información: <https://manned.org/nix3-shell>.

- Inicia un shell interactivo con unos paquetes de `nixpkgs`:

`nix shell {{nixpkgs#pkg1 nixpkgs#packageSet.pkg2 ...}}`

- Inicia un shell que provee un paquete de una versión más antigua de `nixpkgs` (21.05):

`nix shell {{nixpkgs/nixos-21.05#pkg}}`

- Inicia un shell con el "paquete predeterminado" de un flake en el directorio actual, mostrando un registro de construcción si es que algo se construye:

`nix shell -L`

- Inicia un shell con un paquete de un flake en GitHub:

`nix shell {{github:dueño/repositorio#pkg}}`

- Ejecuta un comando en un shell con un paquete:

`nix shell {{nixpkgs#pkg}} -c {{comando --una-bandera 'otros argumentos'}}`
