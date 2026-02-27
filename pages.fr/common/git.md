# git

> Système de gestion de versions décentralisé.
> Certaines commandes comme `commit`, `add`, `branch`, `switch`, `push`, etc. ont leur propre documentation.
> Plus d'informations : <https://git-scm.com/docs/git>.

- Crée un dépôt Git vide :

`git init`

- Clone un dépôt Git distant depuis internet :

`git clone {{https://example.com/repo.git}}`

- Affiche l’état du dépôt local :

`git status`

- Sélectionne les modifications à enregistrer :

`git add {{[-A|--all]}}`

- Enregistre les modifications dans l’historique de versions :

`git commit {{[-m|--message]}} {{texte_du_message}}`

- Envoie les commits locaux vers un dépôt distant :

`git push`

- Récupère les modifications effectuées sur un dépôt distant :

`git pull`

- Réinitialise complètement le dépôt à l’état du dernier commit :

`git reset --hard; git clean {{[-f|--force]}}`
