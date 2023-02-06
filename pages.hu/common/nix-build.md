# nix-build

> Nix-kifejezés létrehozása. További információ: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>.

- Nix-kifejezés építése:

`nix-build '<nixpkgs>' --attr {{firefox}}`

- Sandboxolt Nix-kifejezés építése (nem-NixOS rendszeren):

`nix-build '<nixpkgs>' --attr {{firefox}} --option sandbox true`
