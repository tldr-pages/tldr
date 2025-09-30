# zdb

> ZFS debugger.
> More information: <https://manned.org/zdb>.

- Show detailed configuration of all mounted ZFS zpools:

`zdb`

- Show detailed configuration for a specific ZFS pool:

`zdb {{[-C|--config]}} {{poolname}}`

- Show statistics about number, size and deduplication of blocks:

`zdb {{[-b|--block-stats]}} {{poolname}}`
