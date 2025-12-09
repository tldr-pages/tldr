# git difftool

> Afficher les modifications apportées aux fichiers à l'aide d'outils de comparaison externes. Accepte les mêmes options et arguments que Git diff.
> Plus d'informations : <https://git-scm.com/docs/git-difftool>.

- Lister les outils de comparaison disponibles :

`git difftool --tool-help`

- Configurer Meld comme outil de comparaison par défaut :

`git config --global diff.tool "{{meld}}"`

- Utiliser l'outil de comparaison par défaut pour afficher les fichiers modifiés :

`git difftool --staged`

- Utiliser un outil de comparaison spécifique (opendiff) pour afficher les changements depuis un commit :

`git difftool --tool={{opendiff}} {{commit}}`
