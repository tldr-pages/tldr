# postalias

> Create or update postfix alias databases.
> More information: <https://manned.org/postalias>.

- [c]onfig dir read the main configuration file in the named directory:

`postalias -c {{path/to/config_dir}}`

- Do not [f]old the lookup key to lower case while creating a query table:

`postalias -f`

- Search specific maps for key and [d]elete one entry per map:

`postalias -d "{{key}}"`

- [i]ncremental mode - do not rebuild the database from scratch:

`postalias -i`

- Do [N]ot include the terminating null character that terminates lookup keys and values in the database:

`postalias -N`

- Do not release root privileges when processing a non-root input file:

`postalias -o`
