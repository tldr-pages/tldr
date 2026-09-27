# git format-patch

> Prépare des fichiers de correctifs, utiles pour les envoyer par courriel.
> Voir aussi : `git am`.
> Plus d'informations : <https://git-scm.com/docs/git-format-patch>.

- Crée un fichier de correctif `.patch` nommé automatiquement pour toutes les validations non poussées :

`git format-patch {{origin}}`

- Crée un fichier correctif `.patch` pour les changements entre 2 révisions :

`git format-patch {{revision_1}}..{{revision_2}}`

- Crée un fichier correctif `.patch` pour les 3 dernières validations :

`git format-patch -{{3}}`
