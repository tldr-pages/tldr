# devfsadm

> Administration command for `/dev`. Maintains the `/dev` namespace.
> More information: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Scan for new disks:

`devfsadm -c disk`

- Cleanup any dangling /dev links and scan for new device:

`devfsadm -C -v`

- Dry-run - output what would be changed but make no modifications:

`devfsadm -C -v -n`
