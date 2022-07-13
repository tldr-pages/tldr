# alex

> Un outil qui corrige les phrases insensible et inconsidérée.
> Il vous aide à trouver un genre, une polarité, une éthnie, un blasphème, ou autre inégalité en lisant un texte en anglais.
> Plus d'informations : <https://github.com/get-alex/alex>.

- Analise un texte depuis l'entrée standard :

`echo {{His network looks good}} | alex --stdin`

- Analise tous les fichiers dans le dossier courant :

`alex`

- Analise un fichier spécifique :

`alex {{fichiertexte.md}}`

- Analise tous les fichiers Markdown sauf `exemple.md`

`alex *.md !{{exemple.md}}`
