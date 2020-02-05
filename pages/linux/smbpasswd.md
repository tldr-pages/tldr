# smbpasswd

> Change a user's SMB password.
> Samba users must also have a local Unix account.

- Change the current user's SMB password:

`smbpasswd`

- Add a specified user to Samba and set password(user should already exist in system):

`smbpasswd -a {{username}}`

- Modify an existing Samba user's password:

`smbpasswd {{username}}`

- Delete a Samba user:

`smbpasswd -x {{username}}`
