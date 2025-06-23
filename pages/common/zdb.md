# zdb

> ZFS debugger.
> More information: <https://manned.org/zdb>.

- Show detailed configuration of all mounted ZFS zpools:

`zdb`

- Show detailed [C]onfiguration for a specific ZFS pool:

`zdb -C {{poolname}}`

- Show statistics about number, size and deduplication of [b]locks:

`zdb -b {{poolname}}`
