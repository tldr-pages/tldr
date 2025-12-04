# nix build

> Construit une expression Nix (télécharge depuis le cache si possible).
> Voir aussi : `nix-build` pour des informations sur la construction traditionnelle de Nix, `nix flake` pour des informations sur les flakes.
> Plus d'informations : <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-build.html>.

- Construit un paquet depuis nixpkgs, en liant le résultat symboliquement à `./result`:

`nix build {{nixpkgs#pkg}}`

- Construit un paquet depuis un flake du répertoire actuel, tout en affichant les logs du processus:

`nix build -L {{.#pkg}}`

- Construit le paquet par défaut d'un flake dans un répertoire quelconque:

`nix build {{path/to/directory}}`

- Construit un paquet sans lier le résultat symboliquement, mais affiche le chemin du store dans le `stdout`:

`nix build --no-link --print-out-paths`
