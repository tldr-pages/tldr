# git format-patch

> Préparer des fichiers de correctifs, utiles pour les envoyer par courriel.
> Voir également `git am`, qui peut appliquer des fichiers de correctifs générés.
> Plus d'informations : <https://git-scm.com/docs/git-format-patch>.

- Créer un fichier de correctif `.patch` nommé automatiquement pour tout les commits non poussés :

`git format-patch {{origin}}`

- Créer un fichier correctif `.patch` pour les changements entre 2 révisions :

`git format-patch {{revision_1}}..{{revision_2}}`

- Créer un fichier correctif `.patch` pour les 3 derniers commits :

`git format-patch -{{3}}`
