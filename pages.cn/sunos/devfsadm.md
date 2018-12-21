# devfsadm

> Administration command for `/dev`. Maintains the `/dev` namespace.

- Scan for new disks:

`devfsadm -c disk`

- Cleanup any dangling /dev links and scan for new device:

`devfsadm -C -v`

- Dry-run - output what would be changed but make no modifications:

`devfsadm -C -v -n`
