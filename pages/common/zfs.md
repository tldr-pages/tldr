# zfs

> Manipulate ZFS filesystems

- List all ZFS fileystems 

`zfs list`

- Create filesystems, optionally specifying properties

`zfs create {{pool/filesystem}}`
`zfs create {{-o mountpoint=/path/dir}} {{pool/fileystsem}}`

- Destroy or rename a filesystem/snapshot 

`zfs destroy {{pool/filesystem@snapshot}}`
`zfs rename {{pool/filesystem}} {{pool/filesystem2}}`

- List snapshots, create a snapshot, clone a snapshot to a new filesystem

`zfs list -t snapshot {{pool/filesystem}}`
`zfs snapshot {{pool/filesystem@snapname}}`
`zfs clone {{pool/filesystem@snapname}} {{pool/filesystem2}}

- List/Get/Set various properties

`zfs get all`
`zfs get {{mountpoint,available,compression,compressratio}} {{pool/filesystem}}`
`zfs set {{mountpoint=/path/dir}}`
`zfs set {{compression=on}},{{atime=off}} {{pool/filesystem}}`
