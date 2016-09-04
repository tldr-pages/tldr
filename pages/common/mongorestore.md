# mongorestore

> Utility to import a collection or database from a binary dump into a MongoDB instance.

- Import database from folder containing a bson data dump:

`mongorestore -h {{database_host}} -d {{database_name}} {{path/to/folder}}`

- Import database with user authentication from a folder containing bson data dump:

`mongorestore -h {{database_host}} -d {{database_name}} -u {{username}} -p {{password}} {{path/to/folder}}`

- Import a collection from a .bson file:

`mongorestore -h {{database_host}} -d {{database_name}} {{path/to/file}}`

- Import a collection from a .bson file with user authentication:

`mongorestore -h {{database_host}} -d {{database_name}} -u {{username}} -p {{password}} {{path/to/file}}`
