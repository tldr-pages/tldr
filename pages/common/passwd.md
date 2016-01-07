# passwd

> Passwd is a tool used to change a user's password.

- Change the password of the current user:

`passwd {{new password}}`

- Change the password of the specified user:

`passwd {{username}} {{new password}}`

- Get the current statuts of the user:

`passwd -S`

- Make the password of the account blank (it will set the named account passwordless):

`passwd -d`
