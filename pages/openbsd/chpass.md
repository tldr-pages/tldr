# chpass

> Add or change user database information, including login shell and password.
> See also: `passwd`.
> More information: <https://man.openbsd.org/chsh>.

- Set a specific login shell for the current user interactively:

`doas chsh`

- Set a specific login [s]hell for the current user:

`doas chsh -s {{path/to/shell}}`

- Set a login [s]hell for a specific user:

`doas chsh -s {{path/to/shell}} {{username}}`

- Specify a user database entry in the `passwd` file format:

`doas chsh -a {{username:encrypted_password:uid:gid:...}}`
