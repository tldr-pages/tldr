# nix

> Un puissant gestionnaire de paquets qui rend la gestion des paquets fiable, reproductible et déclarative.
> `nix` est expérimental et doit être activé avec les fonctionnalités expérimentales.
> Voir aussi : `nix classic` pour une interface classique et stable.
> Certaines sous-commandes comme `build`, `develop`, `flake`, `registry`, `profile`, `search`, `repl`, `store`, `edit`, `why-depends`, etc., ont leur propre documentation d'utilisation.
> Plus d'informations : <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix>.

- Activer la commande `nix ` :

`mkdir {{[-p|--parents]}} ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- Rechercher un paquet dans `nixpkgs` par son nom ou sa description :

`nix search nixpkgs {{terme_recherché}}`

- Lancer un terminal avec les paquets spécifiés disponibles depuis `nixpkgs` :

`nix shell {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Installer des paquets depuis `nixpkgs` de manière permanente :

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Nettoyer les chemins inutilisés dans l'espace de stockage de Nix (Nix store) pour libérer de l'espace :

`nix store gc`

- Lancer un environnement interactif pour évaluer des expressions Nix :

`nix repl`

- Afficher l'aide pour une sous-commande spécifique :

`nix help {{sous-commande}}`
