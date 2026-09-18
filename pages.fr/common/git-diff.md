# git diff

> Affiche les changements sur les fichiers suivis.
> Plus d'informations : <https://git-scm.com/docs/git-diff>.

- Affiche les changements sur les fichiers suivis :

`git diff`

- Affiche tous les changements sur les fichiers par rapport à la tête de branche :

`git diff HEAD`

- Affiche tous les changements sur les fichiers ajoutés mais pas encore validés :

`git diff --staged`

- Affiche les changements de tous les validations à partir d'une date / heure donnée (expression de dates, ex : "1 week 2 days" pour 1 semaine et 2 jours ou une date ISO) :

`git diff 'HEAD@{{{3 months|weeks|days|hours|seconds ago}}}'`

- Affiche seulement les noms des fichiers modifiés depuis une validation donnée :

`git diff --name-only {{validation}}`

- Affiche un résumé des créations de fichiers, renommages ou changements de droits depuis une validation :

`git diff --summary {{validation}}`

- Compare un fichier entre deux branches ou validations :

`git diff {{branche_1}}..{{branche_2}} {{chemin/vers/fichier}}`

- Compare plusieurs fichiers de la branche courante avec une autre branche :

`git diff {{branche}}:{{chemin/vers/fichier2}} {{chemin/vers/fichier}}`
