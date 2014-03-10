# zfs

> Manipulate ZFS filesystems

- List, create, destroy ZFS fileystems

`zfs list`
`zfs create {{pool/filesystem}} [{{-o caseinsensitivity=insensitive}}]`
`zfs destroy {{pool/filesystem}}`

- List, create or destroy a snapshot, clone a snapshot to a new filesystem

`zfs list -t snapshot`
`zfs snapshot {{pool/filesystem@snapname}}`
`zfs destroy {{pool/filesystem@snapname}}`
`zfs clone {{pool/filesystem@snapname}} {{pool/filesystem2}}`

- List/Get/Set properties

`zfs get all`
`zfs set {{mountpoint=/path/dir}} {{pool/filesystem}}`
