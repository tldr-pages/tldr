# xfs_admin

> Tune an XFS filesystem.
> More information: <https://manned.org/xfs_admin>.

- Display the filesystem label:

`sudo xfs_admin {{[-l|--list]}} {{/dev/sdX}}`

- Set the filesystem label:

`sudo xfs_admin {{[-L|--Label]}} "{{label}}" {{/dev/sdX}}`

- Display the filesystem UUID:

`sudo xfs_admin {{[-u|--uuid]}} {{/dev/sdX}}`

- Set the filesystem UUID (use with caution):

`sudo xfs_admin {{[-U|--UUID]}} {{uuid}} {{/dev/sdX}}`

- Generate a new UUID for the filesystem:

`sudo xfs_admin {{[-U|--UUID]}} generate {{/dev/sdX}}`

- Display help:

`xfs_admin`
