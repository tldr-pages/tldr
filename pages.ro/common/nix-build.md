# nix-build

> Construiți o expresie Nix.
> Mai multe informaţii: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>

- Construiește o expresie Nix:

`nix-build --attr {{expression_name}}`

- Construiți o expresie Nix sandbox (pe non-NixOS):

`nix-build --attr {{expression_name}} --option sandbox true`
