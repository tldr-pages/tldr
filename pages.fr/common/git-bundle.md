# git bundle

> Empaquetez des objets et des références dans une archive.
> Plus d'informations: <https://git-scm.com/docs/git-bundle>.

- Empaquetez tout les objets et les refferences d'une branche spécifiée:

`git bundle create {{path/to/file.bundle}} {{branch_name}}`

- Crée un empaquetage de tout les fichiers de toutes les branches:

`git bundle create {{path/to/file.bundle}} --all`

- Crée un empaquetage des 5 derniers commits de la branche courrante:

`git bundle create {{path/to/file.bundle}} -{{5}} {{HEAD}}`

- Crée un empaquetage des 7 derniers jours:

`git bundle create {{path/to/file.bundle}} --since={{7.days}} {{HEAD}}`

- Verifie qu'un empaquetage est valide et peut étre appliquer à la branche courrante:

`git bundle verify {{path/to/file.bundle}}`

- Affiche sur la sortie standard la liste des réfferences contenues dans un empaquetage:

`git bundle unbundle {{path/to/file.bundle}}`

- Extraire une branche spécifique d'un fichier de bundle dans le référentiel actuel:

`git pull {{path/to/file.bundle}} {{branch_name}}`
