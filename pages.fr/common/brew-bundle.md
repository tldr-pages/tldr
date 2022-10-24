# brew bundle

> Gestionnaire de paquets pour Homebrew, Homebrew Cask et le Mac App Store.
> Plus d'informations : <https://github.com/Homebrew/homebrew-bundle>.

- Installe tous les paquets listés dans le Brewfile situé dans le dossier courant :

`brew bundle`

- Installe tous les paquets listés dans le Brewfile situé au chemin spécifié :

`brew bundle --file={{chemin/vers/fichier}}`

- Créé un Brewfile avec tous les paquets installés actuellement :

`brew bundle dump`

- Désinstalle tous les paquets non listés dans le Brewfile :

`brew bundle cleanup --force`

- Vérifie si il y a un ou plusieurs paquets à installer ou à mettre à jour depuis le Brewfile :

`brew bundle check`

- Affiche la liste de toutes les entrées dans un Brewfile :

`brew bundle list --all`
