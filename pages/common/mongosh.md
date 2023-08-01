# mongosh

> A new shell for MongoDB, replacement for `mongo`.
> Note: all connection options can be replaced with one string: `mongodb://user@host:port/db_name?authSource=authdb_name`.
> More information: <https://www.mongodb.com/docs/mongodb-shell>.

- Connect to a local database on the default port (`mongodb://localhost:27017`):

`mongosh`

- Connect to a database:

`mongosh --host {{host}} --port {{port}} {{db_name}}`

- Authenticate using the specified username on the specified database (you will be prompted for a password):

`mongosh --host {{host}} --port {{port}} --username {{username}} --authenticationDatabase {{authdb_name}} {{db_name}}`

- Evaluate a JavaScript expression on a database:

`mongosh --eval '{{JSON.stringify(db.foo.findOne())}}' {{db_name}}`
