# brew --cask

> Outil en lignes de commande pour gérer les applications macOS distribuées sous forme de binaires.
> Cette commande remplace `brew cask`, qui a été dépréciée en faveur de `brew --cask`.
> Plus d'informations : <https://github.com/Homebrew/homebrew-cask>.

- Recherche une formule (c.a.d. un package) et/ou un casks (c.a.d une application native) :

`brew search {{texte}}`

- Installe un cask :

`brew install --cask {{nom_du_cask}}`

- Liste les casks installés :

`brew list --cask`

- Liste les casks installés qui ont une nouvelle version disponible :

`brew outdated --cask`

- Met à jour le cask précisé (si aucun nom de cask n'est précisé, tous seront mis à jour) :

`brew upgrade --cask {{nom_du_cask}}`

- Désinstalle un cask :

`brew uninstall --cask {{nom_du_cask}}`

- Désinstalle un cask et supprime les paramètres et fichiers associés :

`brew zap --cask {{nom_du_cask}}`

- Affiche les informations d'un cask en particulier :

`brew info --cask {{nom_du_cask}}`
