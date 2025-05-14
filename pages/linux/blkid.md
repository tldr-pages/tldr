# blkid

> List all recognized partitions and their Universally Unique Identifier (UUID).
> More information: <https://manned.org/blkid>.

- List all partitions:

`sudo blkid`

- List all partitions in a table, including current mountpoints:

`sudo blkid {{[-o|--output]}} list`

- Get the block ID of a partition:

`blkid {{[-s|--match-tag]}} UUID {{[-o|--output]}} value {{/dev/sdXY}}`
