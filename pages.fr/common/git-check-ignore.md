# git check-ignore

> Analyser et déboguer les fichiers ignorés / exclus (".gitignore") de Git.
> Plus d'informations : <https://git-scm.com/docs/git-check-ignore>.

- Verifie qu'un fichier ou repertoire est ignoré :

`git check-ignore {{chemin/vers/fichier_ou_repertoire}}`

- Verifie que plusieurs fichiers ou repertoires sont ignorés :

`git check-ignore {{chemin/vers/fichier}} {{chemin/vers/repertoire}}`

- Utilisez des chemins d'accès, un par ligne, de stdin :

`git check-ignore --stdin < {{chemin/vers/fichier_annexe}}`

- Ne pas vérifier l'index (utilisé pour déboguer pourquoi les chemins ont été suivis et non ignorés) :

`git check-ignore --no-index {{chemin/vers/fichiers_ou_repertoires}}`

- Inclure les details pour chaque occurence dans le chemin :

`git check-ignore --verbose {{chemin/vers/fichiers_ou_repertoires}}`
