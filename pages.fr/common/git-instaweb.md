# git instaweb

> Outil pour le lancement d'un serveur gitweb.
> Plus d'informations : <https://git-scm.com/docs/git-instaweb>.

- Démarre un serveur gitweb depuis le dépôt (`repository`) courant :

`git instaweb --start`

- Écoute uniquement sur le port localhost :

`git instaweb --start {{[-l|--local]}}`

- Écoute sur un port spécifique :

`git instaweb --start {{[-p|--port]}} {{1234}}`

- Utiliser un daemon HTTP spécifique :

`git instaweb --start {{[-d|--httpd]}} {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Lancer en même temps qu'un navigateur web :

`git instaweb --start {{[-b|--browser]}}`

- Stoppe le serveur :

`git instaweb --stop`

- Redémarre le serveur :

`git instaweb --restart`
