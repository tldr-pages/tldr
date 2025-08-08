# bindfs

> Mount a directory elsewhere with different permissions.
> More information: <https://bindfs.org/docs/bindfs.1.html>.

- Mount a directory with same permissions:

`sudo bindfs {{path/to/directory}} {{path/to/mount_point}}`

- Mount a directory elsewhere with the mount directory being owned by another user:

`sudo bindfs --force-user=asd {{path/to/directory}} {{path/to/mount_point}}`

- Unmount a directory:

`sudo umount {{path/to/mount_point}}`
