# nix

> Utilities for the Nix language and store.
> More information: <https://nixos.org>.

- Search for a package via its name or description:

`nix search {{search_term}}`

- Start a Nix shell with the specified packages available:

`nix run {{nixpkgs.pkg1 nixpkgs.pkg2 nixpkgs.pkg3...}}`

- Optimise Nix store disk usage by combining duplicate files:

`nix optimise-store`

- Start an interactive environment for evaluating Nix expressions:

`nix repl`

- Upgrade Nix to the latest stable version:

`nix upgrade-nix`
