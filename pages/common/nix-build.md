# nix-build

> Build a Nix expression.
> More information: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>.

- Build a Nix expression:

`nix-build '<nixpkgs>' --attr {{firefox}}`

- Build a sandboxed Nix expression (on non-NixOS):

`nix-build '<nixpkgs>' --attr {{firefox}} --option sandbox true`
