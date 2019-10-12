# smbpasswd

> Change a user's SMB password.

- Change current user's SMB password:

`smbpasswd`

- Add specified user to Samba and set password(user should already exist in system):

`smbpasswd -a {{user_name}}`

- Modify an existing Samba user's password:

`smbpasswd {{user_name}}`

- Delete Samba user:

`smbpasswd -x {{user_name}}`
