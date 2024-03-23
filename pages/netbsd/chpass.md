# chpass

> Add or change user database information, including login shell and password.
> See also: `passwd`.
> More information: <https://man.openbsd.org/chsh>.

- Set a specific login shell for the current user interactively:

`su -c chpass`

- Set a specific login [s]hell for the current user:

`chpass -s {{path/to/shell}}`

- Set a login [s]hell for a specific user:

`chpass chsh -s {{path/to/shell}} {{username}}`

- Specify a user database entry in the `passwd` file format:

`su -c 'chpass -a {{username:encrypted_password:uid:gid:...}} -s {{path/to/file}}' {{username}}`

- Only update the [l]ocal password file:

`su -c 'chpass -l -s {{path/to/shell}}' {{username}}`

- Forcedly change the database [y]P password database entry:

`su -c 'chpass -y -s {{path/to/shell}}' {{username}}`
