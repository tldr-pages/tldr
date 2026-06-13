# login

> Démarre une session pour un utilisateur.
> Plus d'informations : <https://manned.org/login>.

- Démarrer une session en tant qu'utilisateur :

`login {{utilisateur}}`

- Démarrer une session en tant qu'utilisateur sans authentification si jamais l'utilisateur est déjà pré-authentifié :

`login -f {{utilisateur}}`

- Démarrer une session en tant qu'utilisateur et en préservant l'environnement courant :

`login -p {{utilisateur}}`

- Démarrer une session en tant qu'utilisateur sur un hôte distant :

`login -h {{hote}} {{utilisateur}}`
