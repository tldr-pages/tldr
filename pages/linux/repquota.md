# repquota

> Display a summary of existing file quotas for a filesystem.
> More information: <https://manned.org/repquota>.

- Report stats for all quotas in use:

`sudo repquota -all`

- Report quota stats for all users, even those who aren't using any of their quota:

`sudo repquota -v {{path/to/file}}`

- Report on quotas for users only:

`repquota --user {{path/to/file}}`

- Report on quotas for groups only:

`sudo repquota --group {{path/to/file}}`

- Report on used quota and limits in a human-readable format:

`sudo repquota --human-readable {{path/to/file}}`

- Report on all quotas for users and groups in a human-readable format:

`sudo repquota -augs`
