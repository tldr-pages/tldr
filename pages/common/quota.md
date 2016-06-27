# quota

> Display users' disk space usage and allocated limits.

- Show disk quotas for the current user:

`quota`

- Verbose output (also display quotas on filesystems where no storage is allocated):

`quota -v`

- Quiet output (only display quotas on filesystems where usage is over quota):

`quota -q`

- Print quotas for the groups of which the current user is a member:

`quota -g`

- Show disk quotas for another user (must be superuser to do this):

`sudo quota -u {{username}}`
