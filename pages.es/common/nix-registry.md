# nix registry

> Administra un registro de un flake de nix.
> Vea tambiém: `nix flake` para información sobre los flakes.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-registry.html>.

- Fija la revisión de `nixpkgs` a la versión actual del repositorio upstream:

`nix registry pin {{nixpkgs}}`

- Fija una entrada a la versión actual de la rama, o una revisión particular de un repositorio de GitHub:

`nix registry pin {{entrada}} {{github:dueño/repositorio/rama_o_revisión}}`

- Añade una entrada nueva que siempre apunta a la versión más reciente de un repositorio de GitHub, actualizando automáticamente:

`nix registry add {{entrada}} {{github:dueño/repositorio}}`

- Quita una entrada del registro:

`nix registry remove {{entrada}}`

- Vea la documentación sobre lo que son los registros de flakes de nix:

`nix registry --help`
