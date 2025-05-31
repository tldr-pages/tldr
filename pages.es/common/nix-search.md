# nix search

> Busca paquetes en un flake de Nix.
> Vea también: `nix flake` para información sobre los flakes.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-search.html>.

- Busca `nixpkgs` para un paquete basado en su nombre o descripción:

`nix search {{nixpkgs}} {{término_de_búsqeda}}`

- Muestra la descripción de un paquete de nixpkgs:

`nix search {{nixpkgs#pkg}}`

- Muestra todos los paquetes disponibles de un flake en Github:

`nix search {{github:dueño/repositorio}}`
