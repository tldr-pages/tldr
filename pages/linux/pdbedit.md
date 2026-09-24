# pdbedit

> Edit the Samba user database.
> For simple user add/remove/password, you can also use `smbpasswd`.
> More information: <https://manned.org/pdbedit>.

- List all Samba users:

`sudo pdbedit {{[-L|--list]}}`

- List all Samba users and their settings:

`sudo pdbedit {{[-L|--list]}} {{[-v|--verbose]}}`

- Add an existing Unix user to Samba (will prompt for password):

`sudo pdbedit {{[-u|--user]}} {{username}} {{[-a|--create]}}`

- Remove a Samba user:

`sudo pdbedit {{[-u|--user]}} {{username}} {{[-x|--delete]}}`

- Reset a Samba user's failed password counter:

`sudo pdbedit {{[-u|--user]}} {{username}} {{[-z|--bad-password-count-reset]}}`
