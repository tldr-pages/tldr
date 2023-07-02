# postalias

> Create or update Postfix alias databases.
> More information: <https://manned.org/postalias>.

- Read the main configuration file in the named directory instead of the default configuration directory:

`postalias -c {{path/to/config_directory}}`

- Do not fold the lookup key to lowercase while creating a query table:

`postalias -f`

- Search specific maps for the key and delete one entry per map:

`postalias -d "{{key}}"`

- Read entries from standard input and do not truncate an existing database:

`postalias -i`

- Include the terminating null character that terminates lookup keys and values in the database:

`postalias -N`

- Do not release root privileges when processing a non-root input file:

`postalias -o`
