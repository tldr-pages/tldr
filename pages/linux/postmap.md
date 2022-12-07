# postmap

> Create or query one or more Postfix lookup tables, or update an existing one.
> More information: <https://manned.org/postmap>.

- Search specified maps for the key and remove one entry per map:

`postmap -d {{key}} {{input_file}}`

- Enable message header query mode:

`postmap -h {{input_file}}`

- Search specified maps for the key and write the first value found to the standard output stream:

`postmap -q {{key}} {{input_file}}`

- Retrieve all database elements, and write one line of key value output for each element:

`postmap -s {{input file}}`

- Disable UTF-8 support:

`postmap -u`
