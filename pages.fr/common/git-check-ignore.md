# git check-ignore

> Analyser et déboguer les fichiers ignorés / exclus (".gitignore") de Git.
> Plus d'informations : <https://git-scm.com/docs/git-check-ignore>.

- Vérifie qu'un fichier ou répertoire est ignoré :

`git check-ignore {{chemin/vers/fichier_ou_répertoire}}`

- Vérifie que plusieurs fichiers ou répertoires sont ignorés :

`git check-ignore {{chemin/vers/fichier}} {{chemin/vers/répertoire}}`

- Utilisez des chemins d'accès, un par ligne, de stdin :

`git check-ignore --stdin < {{chemin/vers/fichier_annexe}}`

- Ne pas vérifier l'index (utilisé pour déboguer pourquoi les chemins ont été suivis et non ignorés) :

`git check-ignore --no-index {{chemin/vers/fichiers_ou_répertoires}}`

- Inclure les détails pour chaque occurrence dans le chemin :

`git check-ignore --verbose {{chemin/vers/fichiers_ou_répertoires}}`
