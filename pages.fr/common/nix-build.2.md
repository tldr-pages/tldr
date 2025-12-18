# nix-build

> Construit une expression Nix.
> Voir aussi : `nix build.3`.
> Plus d'informations : <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

- Construit une expression Nix :

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}}`

- Construit une expression Nix en mode bac à sable (sur un système non-NixOS) :

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}} --option sandbox true`
