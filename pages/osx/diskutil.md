# diskutil

> Utility to manage local disks and volumes.

- List all currently available disks, partitions and mounted volumes:

`diskutil list`

- Repair the file system data structures of a volume:

`diskutil repairVolume {{/dev/diskX}}`

- Unmount a volume:

`diskutil unmountDisk {{/dev/diskX}}`

- Eject a CD/DVD (unmount first):

`diskutil eject {{/dev/disk1}}`
