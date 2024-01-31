# diskutil

> Utility to manage local disks and volumes.
> More information: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- List all currently available disks, partitions and mounted volumes:

`diskutil list`

- Repair the filesystem data structures of a volume:

`diskutil repairVolume {{/dev/disk_device}}`

- Unmount a volume:

`diskutil unmountDisk {{/dev/disk_device}}`

- Eject a CD/DVD (unmount first):

`diskutil eject {{/dev/disk_device1}}`
