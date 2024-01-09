# mongo

> Cliente shell interativo de MongoDB.
> Mais informações: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Conecta a uma base de dados local na porta padrão (mongodb://localhost:27017):

`mongo`

- Conecta a uma base de dados em um host e porta específicos:

`mongo --host {{host}} --port {{porta}} {{base_de_dados}}`

- Autentica usando, na base de dados especificada, o nome de usuário especificado (uma senha será solicitada):

`mongo --host {{host}} --port {{porta}} --username {{usuário}} --authenticationDatabase {{auth_base_de_dados}} {{base_de_dados}}`

- Avalia JavaScript na base de dados:

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{base_de_dados}}`
