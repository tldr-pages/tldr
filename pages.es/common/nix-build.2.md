# nix-build

> Construye una expresión de Nix.
> Vea también: `nix build.3`.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

- Construye una expresión de Nix:

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}}`

- Construye una expresión de Nix aislada (en sistemas que no son NixOS):

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}} --option sandbox true`
