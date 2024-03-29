# mkfs.f2fs

> Creates an F2FS filesystem inside a partition.
> More information: <https://manned.org/mkfs.f2fs>.

- Create an F2FS filesystem inside partition 1 on device b (`sdb1`):

`sudo mkfs.f2fs {{/dev/sdb1}}`

- Create an F2FS filesystem with a volume label:

`sudo mkfs.f2fs -l {{volume_label}} {{/dev/sdb1}}`
