# zfs

> Manipulate ZFS filesystems

- List, create, destroy or rename ZFS fileystems

`zfs list`
`zfs create {{pool/filesystem}}`
`zfs destroy {{pool/filesystem}}`
`zfs rename {{pool/filesystem}} {{pool/filesystem2}}`

- List, create or destroy a snapshot, clone a snapshot to a new filesystem

`zfs list -t snapshot`
`zfs snapshot {{pool/filesystem@snapname}}`
`zfs destroy {{pool/filesystem@snapname}}`
`zfs clone {{pool/filesystem@snapname}} {{pool/filesystem2}}`

- List/Get/Set properties

`zfs get all`
`zfs get {{mountpoint,available,compression,compressratio}} {{pool/filesystem}}`
`zfs set {{mountpoint=/path/dir}},{{compression=on}},{{atime=off}} {{pool/filesystem}}`
