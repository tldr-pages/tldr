# repquota

> Display a summary of existing file quotas for a filesystem.

- Report stats for all quotas in use:

`sudo repquota -all`

- Report quota stats for all users, even those who aren't using any of their quota:

`sudo repquota -v`

- Report on quotas for current user:

`repquota --user {{current_user}}`

- Report on quotas for another user:

`sudo repquota --user {{another_user}}`

- Report on quotas for user groups:

`sudo repquota --group {{group}}`

- Report on used quota and limits in a human-readable format:

`sudo repquota --human-readable {{filesystem}}`

- Report on all quotas for users and groups in a human-readable format:

`sudo repquota -augs {{filesystem}}`
