# chpass

> Add or change user database information, including login shell and password.
> See also: `passwd`.
> More information: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Add or change user database information for the current user interactively:

`su -c chpass`

- Set a specific login [s]hell for the current user:

`chpass -s {{path/to/shell}}`

- Set a login [s]hell for a specific user:

`chpass -s {{path/to/shell}} {{username}}`

- Change the account [e]xpire time (in seconds from the epoch, UTC):

`su -c 'chpass -e {{time}} {{username}}'`

- Change a user's password:

`su -c 'chpass -p {{encrypted_password}} {{username}}'`

- Specify the [h]ostname or address of an NIS server to query:

`su -c 'chpass -h {{hostname}} {{username}}'`

- Specify a particular NIS [d]omain (system domain name by default):

`su -c 'chpass -d {{domain}} {{username}}'`
