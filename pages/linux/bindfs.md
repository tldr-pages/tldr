# bindfs

> Mount a directory elsewhere with different permissions.
> More information: <https://manned.org/a2disconf.8>.

- Mount a directory with same permissions:

`sudo bindfs {{path/to/directory}} {{path/to/bind}}`

- Mount a directory elsewhere with the mount directory being owned by another user:

`sudo bindfs --force-user=asd {{path/to/directory}} {{path/to/bind}}`

- Unmount a directory:

`sudo umount {{path/to/bind}}`
