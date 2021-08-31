# zfs

> Manage ZFS filesystems.
> More information: <https://docs.oracle.com/cd/E23823_01/html/819-5461/zfsover-2.html>.

- List all available zfs filesystems:

`zfs list`

- Create a new ZFS filesystem:

`zfs create {{pool_name/filesystem_name}}`

- Delete a ZFS filesystem:

`zfs destroy {{pool_name/filesystem_name}}`

- Create a Snapshot of a ZFS filesystem:

`zfs snapshot {{pool_name/filesystem_name}}@{{snapshot_name}}`

- Enable compression on a filesystem:

`zfs set compression=on {{pool_name/filesystem_name}}`

- Change mountpoint for a filesystem:

`zfs set mountpoint={{/my/mount/path}} {{pool_name/filesystem_name}}`
