# mongo

> Cliente shell interativo de MongoDB.
> Mais informações: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Conecta a uma base de dados:

`mongo`

- Conecta a uma base de dados em um host e porta específicos:

`mongo --host {{host}} --port {{porta}} {{base_de_dados}}`

- Conecta a uma base de dados com um usuário específico, uma senha será pedida ao usuário:

`mongo --host {{host}} --port {{porta}} --username {{usuário}} --authenticationDatabase {{auth_base_de_dados}} {{base_de_dados}}`

- Avalia JavaScript na base de dados:

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{base_de_dados}}`
