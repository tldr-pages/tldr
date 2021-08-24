# diskutil

> Utility to manage local disks and volumes.
> More information: <https://ss64.com/osx/diskutil.html>.

- List all currently available disks, partitions and mounted volumes:

`diskutil list`

- Repair the filesystem data structures of a volume:

`diskutil repairVolume {{/dev/diskX}}`

- Unmount a volume:

`diskutil unmountDisk {{/dev/diskX}}`

- Eject a CD/DVD (unmount first):

`diskutil eject {{/dev/disk1}}`
