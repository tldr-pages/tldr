# mongo

> Client shell pour MongoDB.
> Plus d'informations : <https://docs.mongodb.com/manual/reference/program/mongo>.

- Connecte à une base de données (database) :

`mongo {{nom_de_la_base_de_données}}`

- Connecte à une base de données (database) sur un hôte (host) distant et un port donné :

`mongo --host {{hôte}} --port {{port}} {{nom_de_la_base_de_données}}`

- Connecte à une base de données (database) avec un nom d'utilisateur (username); L'utilisateur sera invité à saisir son mot de passe :

`mongo --username {{nom_d'utilisateur}} {{nom_de_la_base_de_données}} --password`

- Évalue une expression JavaScript sur une base de données (database) :

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{nom_de_la_base_de_données}}`
