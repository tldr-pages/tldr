# git check-ignore

> Analyser et déboguer les fichiers ignorés / exclus (".gitignore") de Git.
> Plus d'informations: <https://git-scm.com/docs/git-check-ignore>.

- Verifie qu'un fichier ou repertoire est ignoré:

`git check-ignore {{path/to/file_or_directory}}`

- Verifie que plusieurs fichiers ou repertoires sont ignorés:

`git check-ignore {{path/to/file}} {{path/to/directory}}`

- Utilisez des chemins d'accès, un par ligne, de `stdin`:

`git check-ignore --stdin < {{path/to/file_list}}`

- Ne pas vérifier l'index (utilisé pour déboguer pourquoi les chemins ont été suivis et non ignorés):

`git check-ignore --no-index {{path/to/files_or_directories}}`

- Inclure les details pour chaque occurence dans le chemin:

`git check-ignore --verbose {{path/to/files_or_directories}}`
