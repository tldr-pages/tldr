# blkid

> List all recognized partitions and their Universally Unique Identifier (UUID).
> More information: <https://manned.org/blkid>.

- List all partitions:

`sudo blkid`

- List all partitions in a user friendly table, including current mountpoints:

`sudo blkid {{[-o|--output]}} list`

- Print only a specific tag:

`sudo blkid {{[-s|--match-tag]}} {{UUID|TYPE|LABEL|...}}`

- List devices with a specific filesystem type:

`sudo blkid {{[-t|--match-token]}} TYPE={{ext4}}`

- Get the UUID of the filesystem on a partition:

`sudo blkid {{[-s|--match-tag]}} UUID {{[-o|--output]}} value {{/dev/sdXY}}`
