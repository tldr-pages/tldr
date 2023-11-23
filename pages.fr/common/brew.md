# brew

> Gestionnaire de paquets pour macOS et Linux.
> Plus d'informations : <https://docs.brew.sh/Manpage>.

- Installe la dernière version stable d'une formule ou d'un cask (ajouter `--devel` pour une version de développement):

`brew install {{formule}}`

- Liste toutes les formules et les casks installés :

`brew list`

- Met à jour une formule ou cask déjà installé (si rien n'est précisé, toutes les formules et tous les casks installés seront mis à jour) :

`brew upgrade {{formule}}`

- Récupère la dernière version d'Homebrew et toutes les formules et casks depuis le dépôt source d'Homebrew :

`brew update`

- Montre les formules et les casks disposants d'une nouvelle version :

`brew outdated`

- Recherche une formule (c.a.d. un package) et/ou un cask (c.a.d une application native) :

`brew search {{texte}}`

- Affiche les informations d'une formule ou d'un cask (version, chemin d'installation, dépendances, etc.) :

`brew info {{formule}}`

- Vérifie que l'installation locale d'Homebrew n'a pas de problème :

`brew doctor`
