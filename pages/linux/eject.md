# eject

> Eject cds, floppy disks and tape drives.

- Display the default device:

`eject -d`

- Eject the default device:

`eject`

- Eject a specific device (the default order is cd-rom, scsi, floppy and tape):

`eject {{/dev/cdrom}}`

- Toggle whether a device's tray is open or closed:

`eject -T {{name_of_device}}`

- Eject a cd drive:

`eject -r {{name_of_device}}`

- Eject a floppy drive:

`eject -f {{name_of_device}}`

- Eject a tape drive:

`eject -q {{name_of_device}}`
