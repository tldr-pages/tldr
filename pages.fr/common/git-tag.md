# git tag

> Créer, lister, verifier et suprimer des tags.
> Un tag est une reférence statique vers un commit.
> Plus d'informations: <https://git-scm.com/docs/git-tag>.

- Lister tout les tags:

`git tag`

- Créer un tag avec le nom donné pointant vers le commit actuel:

`git tag {{tag_name}}`

- Créer un tag avec le nom donné pointant vers un commit spécifié:

`git tag {{tag_name}} {{commit}}`

- Créer un tag annoté avec le message spécifié:

`git tag {{tag_name}} -m {{tag_message}}`

- Suprimer le tag avec le nom spécifié:

`git tag -d {{tag_name}}`

- Metre a jour les tags depuis l'origine:

`git fetch --tags`

- Liste toutes les tags dont les ancêtres incluent un commit donné:

`git tag --contains {{commit}}`
