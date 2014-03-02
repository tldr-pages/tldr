# zpool

> Manage ZFS pools

- Show the configuration and status of all ZFS zpools

`zpool status [{{poolname}}]`

- Check a ZFS pool for errors (reads and verifies the checksum of EVERY block).

`zpool scrub {{poolname}}`

- List available zpools, import a zpool, import optionally specifying a new name.

`zpool import`
`zpool import {{poolname}}`
`zpool import {{poolname}} {{newpoolname}}`

- Export a zpool (unmount all filesystems)

`zpool export {{poolname}}`

- Show the history of all pool operations

`zpool histrory {{poolname}}`

- Create a mirrored pool. 

`zpool create {{poolname}} mirror {{disk1}} {{disk2}}`
`zpool create {{poolname}} mirror {{disk1}} {{disk2}} mirror {{disk3}} {{disk4}}`
