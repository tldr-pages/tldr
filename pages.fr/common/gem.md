# gem

> Un gestionnaire de paquets pour le langage de programmation Ruby.
> Plus d'informations : <https://guides.rubygems.org>.

- Recherche des gems distantes et affiche toutes les versions disponibles :

`gem search {{expression_régulière}} --all`

- Installe la dernière version d'une gem :

`gem install {{nom_gem}}`

- Installe une version spécifique d'une gem :

`gem install {{nom_gem}} --version {{1.0.0}}`

- Installe la dernière version correspondante (SemVer) d'une gem :

`gem install {{nom_gem}} --version '~> {{1.0}}'`

- Mise à jour d'une gem :

`gem update {{nom_gem}}`

- Liste toutes les gems locales :

`gem list`

- Désinstalle une gem :

`gem uninstall {{nom_gem}}`

- Désinstalle une version spécifique d'une gem :

`gem uninstall {{nom_gem}} --version {{1.0.0}}`
