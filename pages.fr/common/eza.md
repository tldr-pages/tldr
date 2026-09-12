# eza

> Une alternative moderne et régulièrement mise à jour à `ls`, basée sur `exa`.
> Plus d'informations : <https://github.com/eza-community/eza>.

- Liste les fichiers, un par ligne :

`eza {{[-1|--oneline]}}`

- Liste tous les fichiers, ainsi que les fichiers cachés :

`eza {{[-a|--all]}}`

- Liste tous les fichiers avec un format détaillé (permissions, propriétaire, taille et date de modification)

`eza {{[-al|--all --long]}}`

- Liste les fichiers les plus lourds en premier:

`eza {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Affichez un arbre de fichiers, sur trois niveaux de profondeur:

`eza {{[-lT|--long --tree]}} {{[-L|--level]}} {{3}}`

- Liste les fichiers par date de modification (les plus âgés en premier)):

`eza {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Liste les fichiers avec une icône et affiche en premier les dossiers (on peut ajouter -l après le eza pour afficher en liste)

`eza --icons --group-directories-first`

- Liste les fichiers avec leurs en-têtes, leurs icônes et leur statut Git:

`eza {{[-lh|--long --header]}} --icons --git`

- Ne liste pas les fichiers qui sont inscrits dans `.gitignore`:

`eza --git-ignore`
