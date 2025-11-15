# nix flake

> Administra los flakes de Nix.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-flake.html>.

- Crea un flake nuevo (solo el archivo `flake.nix`) usando la plantilla predeterminada, en el directorio actual:

`nix flake init`

- Actualiza todos las entradas (dependencias) del flake en el directorio actual:

`nix flake update`

- Actualiza una entrada específica (dependencia) del flake en el directorio actual:

`nix flake update {{entrada}}`

- Muestra todas the salidas de un flake en github:

`nix flake show {{github:dueño/repositorio}}`

- Muestra ayuda:

`nix flake --help`
