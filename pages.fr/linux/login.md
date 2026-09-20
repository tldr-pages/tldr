# login

> Démarre une session pour un utilisateur.
> Plus d'informations : <https://manned.org/login>.

- Démarre une session en tant qu'utilisateur :

`login {{utilisateur}}`

- Démarre une session en tant qu'utilisateur sans authentification si jamais l'utilisateur est déjà pré-authentifié :

`login -f {{utilisateur}}`

- Démarre une session en tant qu'utilisateur et en préservant l'environnement actuel :

`login -p {{utilisateur}}`

- Démarre une session en tant qu'utilisateur sur un hôte distant :

`login -h {{hote}} {{utilisateur}}`
