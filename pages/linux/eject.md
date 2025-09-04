# eject

> Eject CDs, floppy disks, tape drives, and USB sticks.
> More information: <https://manned.org/eject>.

- Display the default device:

`eject {{[-d|--default]}}`

- Eject the default device:

`eject`

- Eject a specific device (the default order is cd-rom, scsi, floppy and tape):

`eject {{/dev/cdrom}}`

- Toggle whether a device's tray is open or closed:

`eject {{[-T|--traytoggle]}} {{/dev/cdrom}}`

- Eject a cd drive:

`eject {{[-r|--cdrom]}} {{/dev/cdrom}}`

- Eject a floppy drive:

`eject {{[-f|--floppy]}} {{/mnt/floppy}}`

- Eject a tape drive:

`eject {{[-q|--tape]}} {{/mnt/tape}}`

- Set whether the physical eject button is [i]gnored (`on` prevents ejecting):

`eject {{[-i|--manualeject]}} {{on|off}}`
