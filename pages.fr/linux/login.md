# login
> Démarre une session pour un utilisateur
> Plus d'informations : <https://manned.org/login>.

- Démarrer une session en tant qu'utilisateur *user* :

`login {{user}}`


- Démarrer une session en tant qu'utilisateur *user* sans authentification si jamais *user* est déjà pré-authentifié:

`login -f {{user}}`


- Démarrer une session en tant qu'utilisateur *user* et en préservant l'environnement courant :

`login -p {{user}}`


- Démarrer une session en tant qu'utilisateure *user* sur un hôte distant :

`login -h {{host}} {{user}}`
