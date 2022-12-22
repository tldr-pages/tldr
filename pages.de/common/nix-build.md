# nix-build

> Erstellen eines Nix-Ausdruck.
> Weitere Informationen: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>.

- Erstellen eines Nix-Ausdrucks:

`nix-build '<nixpkgs>' --attr {{firefox}}`

- Erstellen eines Nix-Ausdruck mit Sandbox (auf nicht-NixOS):

`nix-build '<nixpkgs>' --attr {{firefox}} --option sandbox true`
