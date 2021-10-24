# git diff

> Afficher les changements sur les fichiers suivis.
> Plus d'informations : <https://git-scm.com/docs/git-diff>.

- Afficher les changements sur les fichiers suivis :

`git diff`

- Afficher tous les changements sur les fichiers par rapport à la tête de branche :

`git diff HEAD`

- Afficher tous les changements sur les fichiers ajoutés mais pas encore commités :

`git diff --staged`

- Afficher les changements de tous les commits à partir d'une date / heure donnée (expression de dates, ex : "1 week 2 days" pour 1 semaine et 2 jours ou une date ISO) :

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Afficher seulement les noms des fichiers modifiés depuis un commit donné :

`git diff --name-only {{commit}}`

- Afficher un résumé des créations de fichiers, renommages ou changements de droits depuis un commit :

`git diff --summary {{commit}}`

- Comparer un fichier entre deux branches ou commits :

`git diff {{branche_1}}..{{branche_2}} [--] {{chemin/vers/fichier}}`

- Comparer plusieurs fichiers de la branche courante avec une autre branche :

`git diff {{branche}}:{{chemin/vers/fichier2}} {{chemin/vers/fichier}}`
