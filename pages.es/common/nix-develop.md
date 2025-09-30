# nix develop

> Ejecuta un shell de Bash que provee el entorno de construcción de una derivación.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>.

- Ejecuta un shell con todas las dependencias de un paquete de nixpkgs disponibles:

`nix develop {{nixpkgs#pkg}}`

- Inicia un shell para desarrollo para el paquete predeterminado de un flake en el directorio actual:

`nix develop`

- En ese shell, configura y construye los códigos fuentes:

`configurePhase; buildPhase`
