# nix edit

> Abre la expresión de Nix de un paquete Nix dentro de $EDITOR.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-edit.html>.

- Abre el código fuente de la expresión Nix de un paquete de nixpkgs dentro de tu `$EDITOR`:

`nix edit {{nixpkgs#pkg}}`

- Vuelca el código fuente de un paquete en `stdout`:

`EDITOR=cat nix edit {{nixpkgs#pkg}}`
