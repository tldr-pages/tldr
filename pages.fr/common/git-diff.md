# git diff

> Affiche les modifications sur les fichiers suivis.
> Plus d'informations : <https://git-scm.com/docs/git-diff>.

- Affiche les modifications non indexées :

`git diff`

- Affiche toutes les modifications non validées (y compris celles qui sont indexées) :

`git diff HEAD`

- Affiche uniquement les modifications indexées (ajoutées, mais pas encore validées) :

`git diff --staged`

- Affiche les modifications de toutes les validations à partir d'une date/heure donnée (expression de dates, ex : "1 week 2 days" pour 1 semaine et 2 jours ou une date ISO) :

`git diff 'HEAD@{{{3 months|weeks|days|hours|seconds ago}}}'`

- Affiche les statistiques du diff, comme les fichiers modifiés, l'histogramme et le nombre total de lignes ajoutées/supprimées :

`git diff --stat {{validation}}`

- Affiche un résumé des créations de fichiers, renommages ou changements de mode depuis une validation donnée:

`git diff --summary {{validation}}`

- Compare un fichier entre deux branches ou validations :

`git diff {{branche_1}}..{{branche_2}} {{chemin/vers/fichier}}`

- Compare différents fichiers de la branche actuelle avec une autre branche :

`git diff {{autre_branche}}:{{chemin/vers/fichier2}} {{chemin/vers/fichier1}}`
