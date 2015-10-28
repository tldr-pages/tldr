# zfs

> Manage ZFS filesystems

- List all available zfs filesystems

`zfs list`

- Create a new ZFS filesystem

`zfs create poolname/newfsname`

- Delete a ZFS filesystem

`zfs destroy {{poolname/newfsname}}`

- Create a Snapshot of a ZFS filesystem

`zfs snapshot {{poolname/filesystem@snapshot-name}}`

- Enable compression on a filesystem

`zfs set compression=on {{poolname/fileystem}}`

- Change mountpoint for a filesytem

`zfs set mountpoint={{/my/mount/path}} {{poolname/filesystem}}`
