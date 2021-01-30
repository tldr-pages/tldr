# git instaweb

> Outil pour le lancemend d'un serveur gitweb.
> Plus d'informations : <https://git-scm.com/docs/git-instaweb>.

- Démare un serveur gitweb depuis le repository courrant :

`git instaweb --start`

- Écoute uniquement sur le port localhost :

`git instaweb --start --local`

- Écoute sur un port spécifique :

`git instaweb --start --port {{1234}}`

- Utiliser un daemon http spécifique :

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Lancer en méme temps qu un navigateur web :

`git instaweb --start --browser`

- Stoppe le serveur :

`git instaweb --stop`

- Redémarre le serveur :

`git instaweb --restart`
