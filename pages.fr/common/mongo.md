# mongo

> Client shell pour MongoDB
> Plus d'informations: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Se connecter à une base de données (database):

`mongo {{database}}`

- Se connecter à une base de données (database) sur un hôte distant et un port donné

`mongo --host {{host}} --port {{port}} {{database}}`

- Se connecter à une base de données avec un nom d'utilisateur; L'utilisateur sera invité à saisir son mot de passe:

`mongo --username {{username}} {{database}} --password`

- Évaluer une expression Javascript sur une base de données

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{database}}`
