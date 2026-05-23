# postmap

> Postfix lookup table management.
> Create, query, update, or delete entries in Postfix lookup tables.
> More information: <https://www.postfix.org/postmap.1.html>.

- Create or update a lookup table from its source file using the default database type:

`postmap {{path/to/lookup_table}}`

- Create or update a lookup table with a specific database type:

`postmap {{hash|btree|cdb}}:{{path/to/lookup_table}}`

- Query a lookup table for a key:

`postmap -q {{key}} {{hash|btree|cdb}}:{{path/to/lookup_table}}`

- Delete a key from a lookup table:

`postmap -d {{key}} {{hash|btree|cdb}}:{{path/to/lookup_table}}`

- Print all entries from a lookup table:

`postmap -s {{hash|btree|cdb}}:{{path/to/lookup_table}}`

- Add entries from a file to an existing lookup table without truncating it:

`postmap -i {{hash|btree|cdb}}:{{path/to/lookup_table}} < {{path/to/entries_file}}`
