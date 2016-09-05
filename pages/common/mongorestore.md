# mongorestore

> Utility to import a collection or database from a binary dump into a MongoDB instance.

- Import a bson data dump from a folder to a mongodb instance:

`mongorestore --db {{database_name}} {{path/to/folder}}`

- Import a bson data dump from a folder to a given mongodb database host running at a given port with user authentication; user will be prompted for password:

`mongorestore --host {{database_host:port}}  --db {{database_name}} --username {{username}} {{path/to/folder}} --password`

- Import a collection from a bson file to a mongodb instance:

`mongorestore --db {{database_name}} {{path/to/file}}`

- Import a collection from a bson file to a given mongodb database host running at a given port with user authentication; user will be prompted for password:

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/file}} --password`