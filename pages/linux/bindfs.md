# bindfs

> Mount a directory elsewhere with different permissions.
> More information: <https://bindfs.org/docs/bindfs.1.html>.

- Mount a directory with same permissions:

`sudo bindfs {{path/to/directory}} {{path/to/mount_point}}`

- Map filesystem objects owned by `user1` to be owned by `user2` (also applies in reverse to newly created files):

`sudo bindfs --map={{user1}}/{{user2}} {{path/to/directory}} {{path/to/mount_point}}`

- Unmount a directory:

`sudo umount {{path/to/mount_point}}`
