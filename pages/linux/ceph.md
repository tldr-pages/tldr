# ceph

> Ceph implements object storage on a single distributed computer cluster, and provides interfaces for object, block and file-level storage.
> More information: <https://ceph.io>.

- Check or watch cluster health:

`ceph {{status | -w}}`

- Check cluster usage stats:

`ceph df`

- Get the statistics for the placement groups in your cluster:

`ceph pg dump --format {{plain}}`

- Create a storage pool:

`ceph osd pool create {pool_name} {page_number}`

- Delete a storage pool:

`ceph osd pool delete {pool_name} [--yes-i-really-really-mean-it]`

- Rename a storage pool:

`ceph osd pool rename {current-pool-name} {new-pool-name}`

- Self-repair pool storage:

`ceph pg repair {pool_name}`
