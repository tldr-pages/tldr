# fsck.vfat

> Check and repair an MS-DOS FAT filesystem (FAT12, FAT16, or FAT32). The filesystem should be unmounted.
> See also: `fsck.fat`.
> More information: <https://manned.org/fsck.vfat>.

- Interactively [r]epair a filesystem (this is the default):

`sudo fsck.vfat {{/dev/sdXY}}`

- Check a filesystem and write [n]othing:

`sudo fsck.vfat -n {{/dev/sdXY}}`

- [a]utomatically repair a filesystem, choosing the least destructive fix:

`sudo fsck.vfat -a {{/dev/sdXY}}`

- [l]ist the path of each file that is processed:

`sudo fsck.vfat -l -n {{/dev/sdXY}}`

- Automatically repair a filesystem and mark unreadable clusters as bad:

`sudo fsck.vfat -a -t {{/dev/sdXY}}`

- Display help:

`sudo fsck.vfat --help`
