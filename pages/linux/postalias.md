# postalias

> creates or updates postfix alias databses
> More information: <https://manned.org/postalias.1>.

- Config dir read the main configuration file in the named directory:

`postalias -c `

- Do not fold the lookup key to lower case while creating a query table:

`postalias -f`

- Search the specified maps for key and remove one entry per map:

`postalias -d {{key}}`

- Incremental mode - do not rebuild the database from scratch:

`postalias -i`

- Do not include the terminating null character that terminates lookup keys and values in the database:

`postalias -N`

- Do not release root privileges when processing a non-root input file:

`postalias -o`