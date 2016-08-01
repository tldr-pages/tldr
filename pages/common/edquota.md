# edquota

> Edit quota for a user or group.

- Edit the user quota (default):

`edquota --user {{user}}`

- Edit the group quota:

`edquota --group {{group}}`

- Perform operations on given file system ONLY (default is to perform operations on all file systems with quota):

`edquota --file-system {{filesystem}}`

- Edit the default grace period:

`edquota -t`

- Duplicate a quota to other users:

`edquota -p {{reference_user}} {{destination_user1}} {{destination_user2}}`
