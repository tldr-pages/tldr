# pdbedit

> Directly edit the Samba user database.
> Can do more fancy things than `smbpasswd`.
> More information: <https://manned.org/pdbedit.8>.

- List all Samba users (use verbose flag to shows their settings):

`sudo pdbedit --list --verbose`

- Add an existing Unix user to Samba (will prompt for password):

`sudo pdbedit -u {{username}} --create`

- Remove a Samba user:

`sudo pdbedit -u {{username}} --delete`

- Reset a Samba user's failed password counter:

`sudo pdbedit -u {{username}} --bad-password-count-reset`
