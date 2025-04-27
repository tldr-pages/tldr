# edquota

> Edit quotas for a user or group. By default it operates on all filesystems with quotas.
> Quota information is stored permanently in the `quota.user` and `quota.group` files in the root of the filesystem.
> More information: <https://manned.org/edquota>.

- Edit quota of the current user:

`edquota {{[-u|--user]}} $(whoami)`

- Edit quota of a specific user:

`sudo edquota {{[-u|--user]}} {{username}}`

- Edit quota for a group:

`sudo edquota {{[-g|--group]}} {{group}}`

- Restrict operations to a given filesystem (by default edquota operates on all filesystems with quotas):

`sudo edquota {{[-f|--file-system]}} {{filesystem}}`

- Edit the default grace period:

`sudo edquota {{[-t|--edit-period]}}`

- Duplicate a quota to other users:

`sudo edquota {{[-p|--prototype]}} {{reference_user}} {{destination_user1}} {{destination_user2}}`
