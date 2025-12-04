# nix develop

> Lance un terminal Bash avec l'environnement de construction de la dérivation.
> Plus d'informations : <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>.

- Lance un terminal Bash avec toutes les dépendances d'un paquet disponible dans `nixpkgs`:

`nix develop {{nixpkgs#pkg}}`

- Lance un terminal de développement pour le paquet par défaut dans un flake du répertoire actuel:

`nix develop`

- Configure et construit les sources dans le terminal lancé:

`configurePhase; buildPhase`
