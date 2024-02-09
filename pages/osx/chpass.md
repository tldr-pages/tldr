# chpass

> Add or change user database information, including login shell and password.
> Note: it's not possible to change the user's password on Open Directory systems, use `passwd` instead.
> See also: `passwd`.
> More information: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Add or change user database information for the current user interactively:

`su -c chpass`

- Set a specific login [s]hell for the current user:

`chpass -s {{path/to/shell}}`

- Set a login [s]hell for a specific user:

`chpass -s {{path/to/shell}} {{username}}`

- Edit the user record on the directory node at the given [l]ocation:

`chpass -l {{location}} -s {{path/to/shell}} {{username}}`

- Use the given [u]sername when authenticating to the directory node containing the user:

`chpass -u {{authname}} -s {{path/to/shell}} {{username}}`
