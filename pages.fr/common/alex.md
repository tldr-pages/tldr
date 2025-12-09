# alex

> Un outil qui corrige les phrases insensible et inconsidérée (en Anglais uniquement).
> Il vous aide à trouver un genre, une polarité, une ethnie, un blasphème, ou autre inégalité en lisant un texte en anglais.
> Plus d'informations : <https://github.com/get-alex/alex>.

- Analyse un texte depuis l'entrée standard :

`echo {{His network looks good}} | alex --stdin`

- Analyse tous les fichiers dans le dossier courant :

`alex`

- Analyse un fichier spécifique :

`alex {{fichiertexte.md}}`

- Analyse tous les fichiers Markdown sauf `exemple.md` :

`alex *.md !{{exemple.md}}`
