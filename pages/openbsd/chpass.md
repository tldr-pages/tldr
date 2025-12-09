# chpass

> Add or change user database information, including login shell and password.
> See also: `passwd`.
> More information: <https://man.openbsd.org/chpass>.

- Set a specific login shell for the current user interactively:

`doas chpass`

- Set a specific login [s]hell for the current user:

`doas chpass -s {{path/to/shell}}`

- Set a login [s]hell for a specific user:

`doas chpass -s {{path/to/shell}} {{username}}`

- Specify a user database entry in the `passwd` file format:

`doas chpass -a {{username:encrypted_password:uid:gid:...}}`
