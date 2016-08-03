# mongo

> MongoDB shell client.

- Connect to a database:

`mongo {{database}}`

- Connect to a database running on a given host on a given port:

`mongo --host {{host}} --port {{port}} {{database}}`

- Connect to a database with a given username, user will be prompted for password:

`mongo --username {{username}} {{database}} --password`

- Run queries on the database:

`mongo --eval '{{query}}' {{database}}`
