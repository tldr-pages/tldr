# blkid

> List all recognized partitions and their universally unique identifiers (UUIDs).
> More information: <https://manned.org/blkid>.

- List all partitions:

`sudo blkid`

- List all partitions in a table, including current mount points:

`sudo blkid -o list`

- Get the UUID of the filesystem on a specific partition:

`sudo blkid -s UUID -o value /dev/sdXY`
