# chpass

> Add or change user database information, including login shell and password.
> See also: `passwd`.
> More information: <https://man.freebsd.org/cgi/man.cgi?query=chpass>.

- Add or change user database information for the current user interactively:

`chpass`

- Set a specific login [s]hell for the current user:

`chpass -s {{path/to/shell}}`

- Set a login [s]hell for a specific user:

`chpass -s {{path/to/shell}} {{username}}`

- Change the account [e]xpire time (in seconds from the epoch, UTC):

`su -c 'chpass -e {{time}} {{username}}'`

- Change a user's password:

`su -c 'chpass -p {{encrypted_password}} {{username}}'`
