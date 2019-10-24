# mongo

> Cliente shell interativo de MongoDB.
> Mais informações: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Conectar a uma base de dados:

`mongo {{base_de_dados}}`

- Conectar a uma base de dados em um host e porta específicos:

`mongo --host {{host}} --port {{porta}} {{base_de_dados}}`

- Conectar a uma base de dados com um usuário específico, uma senha será pedida ao usuário:

`mongo --username {{usuário}} {{base_de_dados}} --password`

- Avaliar JavaScript na base de dados:

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{base_de_dados}}`
