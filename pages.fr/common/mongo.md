# mongo

> Client shell pour MongoDB.
> Plus d'informations : <https://docs.mongodb.com/manual/reference/program/mongo>.

- Connecte à une base de données (database) sur un hôte (host) distant et un port donné :

`mongo --host {{hôte}} --port {{port}} {{nom_de_la_base_de_données}}`

- Évalue une expression JavaScript sur une base de données (database) :

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{nom_de_la_base_de_données}}`
