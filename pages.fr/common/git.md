# git

> Système de gestion de versions décentralisé.
> Certaines commandes comme `commit`, `add`, `branch`, `switch`, `push`, etc. ont leur propre documentation.
> Plus d'informations : <https://git-scm.com/docs/git>.

- Créer un dépôt Git vide :

`git init`

- Cloner un dépôt Git distant depuis internet :

`git clone {{https://example.com/repo.git}}`

- Afficher l’état du dépôt local :

`git status`

- Sélectionner les modifications à enregistrer :

`git add {{[-A|--all]}}`

- Enregistrer les modifications dans l’historique de versions :

`git commit {{[-m|--message]}} {{texte_du_message}}`

- Envoyer les commits locaux vers un dépôt distant :

`git push`

- Récupérer les modifications effectuées sur un dépôt distant :

`git pull`

- Réinitialiser complètement le dépôt à l’état du dernier commit :

`git reset --hard; git clean {{[-f|--force]}}`
