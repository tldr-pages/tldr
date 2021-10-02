# mongo

> Client shell pour MongoDB
> Plus d'informations: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Se connecter à une base de données (database):

`mongo {{nom de la base de données}}`

- Se connecter à une base de données (database) sur un hôte (host) distant et un port donné

`mongo --host {{hôte}} --port {{port}} {{nom de la base de données}}`

- Se connecter à une base de données (database) avec un nom d'utilisateur (username); L'utilisateur sera invité à saisir son mot de passe:

`mongo --username {{nom d'utilisateur}} {{nom de la base de données}} --password`

- Évaluer une expression Javascript sur une base de données (database)

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{nom de la base de données}}`
