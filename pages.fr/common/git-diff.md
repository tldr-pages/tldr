# git diff

> Afficher les changements sur les fichiers suivis.
> Plus d'informations : <https://git-scm.com/docs/git-diff>.

- Afficher les changements sur les fichiers suvis :

`git diff`

- Afficher tout les changements sur les fichiers par rapport a la téte de branche :

`git diff HEAD`

- Afficher tout les changements sur les fichiers ajoutés mais pas encore commités :

`git diff --staged`

- Afficher les changements de tout les commits a partir d une date/heure donnée (expression de dates, ex : "1 week 2 days" ou une date ISO) :

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Afficher seulement les noms des fichiers modifiés depuis un commit donné :

`git diff --name-only {{commit}}`

- Afficher un resumé des creation de fichiers, renomages ou changements de droits depuis un commit :

`git diff --summary {{commit}}`

- Comparer un ficheir entre deux branches ou commits :

`git diff {{branche_1}}..{{branche_2}} [--] {{chemin/vers/fichier}}`

- Comparer plusieurs fichiers de la branche courrante avec une autre branche :

`git diff {{branche}}:{{chemin/vers/fichier2}} {{chemin/vers/fichier}}`
