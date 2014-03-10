# zpool

> Manage ZFS pools

- Show the configuration and status of all ZFS zpools

`zpool status [{{poolname}}]`

- Show the history of all pool operations

`zpool histrory {{poolname}}`

- Create a mirrored pool 

`zpool create {{poolname}} mirror {{disk1}} {{disk2}} [mirror {{disk3}} {{disk4}}]`
