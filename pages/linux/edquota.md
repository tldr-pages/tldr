# edquota

> Edit quota for a user or group. By default it operates on all file systems with quotas.
> Quota information is stored permanently in the quota.user and quota.group files in the root of the file system.

- Edit quota of current user:

`edquota {{user}}`

- Edit quota of specific user:

`sudo edquota {{user}}`

- Edit the group quota:

`sudo edquota --group {{group}}`

- Perform operations on given file system ONLY (default is to perform operations on all file systems with quota):

`sudo edquota --file-system {{filesystem}}`

- Edit the default grace period:

`sudo edquota -t`

- Duplicate a quota to other users:

`sudo edquota -p {{reference_user}} {{destination_user1}} {{destination_user2}}`
