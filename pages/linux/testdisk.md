# testdisk

> Scan and recover lost disk partitions.
> See also: `photorec`, `fdisk`.
> More information: <https://www.cgsecurity.org/wiki/TestDisk>.

- Start TestDisk on a specific device (interactive TUI):

`sudo testdisk {{/dev/sdX}}`

- Start TestDisk on a disk image:

`sudo testdisk {{path/to/image.dd}}`

- List partitions and write a log file:

`sudo testdisk /list /log`

- Start TestDisk with debug logging enabled:

`sudo testdisk /debug /log {{/dev/sdX}}`

- Show TestDisk version:

`testdisk /version`
