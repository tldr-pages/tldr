# testdisk

> Scan and repair disk partitions.
> See also: `photorec`, `fdisk`.
> More information: <https://www.cgsecurity.org/wiki/TestDisk_Step_By_Step>.

- Start TestDisk on a specific device:

`sudo testdisk {{/dev/sdb}}`

- Start TestDisk on a disk image:

`sudo testdisk {{path/to/image.dd}}`

- Start TestDisk and create a log file (`testdisk.log`):

`sudo testdisk /log {{/dev/sdb}}`

- List current partitions:

`sudo testdisk /list`

- Display version:

`testdisk /version`
