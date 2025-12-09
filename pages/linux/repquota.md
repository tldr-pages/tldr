# repquota

> Display a summary of existing file quotas for a filesystem.
> More information: <https://manned.org/repquota>.

- Report stats for all quotas in use:

`sudo repquota {{[-a|--all]}}`

- Report quota stats for all users, even those who aren't using any of their quota:

`sudo repquota {{[-v|--verbose]}} {{filesystem}}`

- Report on quotas for users only:

`repquota {{[-u|--user]}} {{filesystem}}`

- Report on quotas for groups only:

`sudo repquota {{[-g|--group]}} {{filesystem}}`

- Report on used quota and limits in a human-readable format:

`sudo repquota {{[-s|--human-readable]}} {{filesystem}}`

- Report on all quotas for users and groups in a human-readable format:

`sudo repquota {{[-augs|--all --user --group --human-readable]}}`
