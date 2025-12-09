# nix why-depends

> Muesta por qué un paquete depende de otro paquete.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>.

- Muestra por qué el sistema actual de NixOS requiere una ruta del almacén específica:

`nix why-depends {{/run/current-system}} {{/nix/store/...}}`

- Muestra por qué un paquete de nixpkgs requiere otro paquete como una dependencia de tiempo de construcción:

`nix why-depends --derivation {{nixpkgs#dependiente}} {{nixpkgs#dependencia}}`
