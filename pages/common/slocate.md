# slocate

> Secure variant of GNU Locate.
> See also: `locate`.
> More information: <https://manned.org/slocate>.

- Enable quiet mode to suppress error messages:

`slocate -q`

- Limit the number of results shown:

`slocate -n {{number}}`

- Build an `slocate` database starting at path `/`:

`slocate -u`

- Build an `slocate` database starting at a given directory:

`slocate -U {{path/to/directory}}`

- Update an `slocate` database using the default `/etc/updatedb.conf` configuration:

`slocate -c`

- Set the security level of `slocate`, with `0` being disabled, and `1` being secure:

`slocate -l {{0|1}}`

- Specify the database that `slocate` should search in:

`slocate {{[-d|--database]}} {{path/to/directory}}`

- Search the `slocate` database using a specific `regex` string:

`slocate {{[-r|--regexp]}} {{regex}}`
