# quota

> Display users' disk space usage and allocated limits.
> More information: <https://manned.org/quota>.

- Show disk quotas in human-readable units for the current user:

`quota {{[-s|--human-readable]}}`

- Verbose output (also display quotas on filesystems where no storage is allocated):

`quota {{[-v|--verbose]}}`

- Quiet output (only display quotas on filesystems where usage is over quota):

`quota {{[-q|--quiet]}}`

- Print quotas for the groups of which the current user is a member:

`quota {{[-g|--group]}}`

- Show disk quotas for another user:

`sudo quota {{[-u|--user]}} {{username}}`
