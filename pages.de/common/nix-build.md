# nix-build

> Erstellen eines Nix-Ausdruck.
> Weitere Informationen: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>.

- Erstellen eines Nix-Ausdrucks:

`nix-build --attr {{ausdruck_name}}`

- Erstellen eines Nix-Ausdruck mit Sandbox (auf nicht-NixOS):

`nix-build --attr {{ausdruck_name}} --option sandbox true`
