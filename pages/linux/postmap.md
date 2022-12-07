# postmap

> Create or query one or more Postfix lookup tables, or updates an existing one.
> More information: <https://manned.org/postmap>.

- Search the specified maps for key and remove one entry per map:

`postmap -d {{key}} {{input file}}`

- Enable message header query mode:

`postmap -h {{input file}}`

- Search the specified maps for key and write the first value found to the standard output stream:

`postmap -q {{key}} {{input file}}`

- Retrieve all database elements, and write one line of key value output for each element:

`postmap -s {{input file}}`

- Disable UTF-8 support:

`postmap -u`
