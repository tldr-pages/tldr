# repquota

> Display a summary of existing file quotas for a filesystem.

- Report on all existing quotas:

`repquota -all`

- Report all quotas, even if there is no usage:

`repquota -v`

- Report on quotas for users (default), only super-user may view quotas which are not their own:

`repquota --user {{user}}`

- Report on quotas for user groups:

`repquota --group {{group}}`

- Report on used space and limits in a human-readable format:

`repquota --human-readable {{filesystem}}`

- Report on all quotas for users and groups in a human-readable format:

`repquota -augs {{filesystem}}`
