# couchdb

> This is the command line interface for Apache CouchDB database server.

- Add a configuration file to chain:

`couchdb -a {{path/to/file}}`

- Add a configuration directory to chain:

`couchdb -A {{path/to/file}}`

- Enter the interactive Erlang shell:

`couchdb -i`

- Redirect output from couchdb.stdout to file:

`couchdb -o {{path/to/file}}`

- Redirect errors from couchdb.stderr to file:

`couchdb -e {{path/to/file}}`

- Display the status of the background process:

`couchdb -s`

- Kill the background process (Note: It will respawn if needed):

`couchdb -k`

- Shutdown the background process:

`couchdb -d`

