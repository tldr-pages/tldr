# smbpasswd

> Add/remove a Samba user or change its password.
> Samba users must have an existing local Unix account.
> More information: <https://manned.org/smbpasswd.8>.

- Change the current user's SMB password:

`smbpasswd`

- Add a specified user to Samba and set password (user should already exist in system):

`sudo smbpasswd -a {{username}}`

- Modify an existing Samba user's password:

`sudo smbpasswd {{username}}`

- Delete a Samba user (use `pdbedit` instead if the Unix account has been deleted):

`sudo smbpasswd -x {{username}}`
