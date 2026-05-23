# postalias

> Postfix alias database maintenance.
> Create, update, query, or delete entries in Postfix alias databases.
> More information: <https://www.postfix.org/postalias.1.html>.

- Create or update the default alias database from an alias source file:

`sudo postalias {{/etc/aliases}}`

- Create or update an alias database with a specific database type:

`sudo postalias {{hash|btree|cdb|dbm|lmdb}}:{{path/to/aliases}}`

- Query an alias and print its mapped value:

`postalias -q {{alias}} {{hash|btree|cdb|dbm|lmdb}}:{{path/to/aliases}}`

- Delete an alias from a database:

`sudo postalias -d {{alias}} {{hash|btree|cdb|dbm|lmdb}}:{{path/to/aliases}}`

- Dump all database entries:

`postalias -s {{hash|btree|cdb|dbm|lmdb}}:{{path/to/aliases}}`

- Add entries from `stdin` without truncating the existing database:

`echo "{{alias}}: {{user@example.com}}" | sudo postalias -i {{hash|btree|cdb|dbm|lmdb}}:{{path/to/aliases}}`
