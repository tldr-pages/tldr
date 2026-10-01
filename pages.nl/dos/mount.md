# MOUNT

> Koppel hostmappen/-schijven/-images als virtuele DOS-schijven.
> Meer informatie: <https://www.dosbox.com/wiki/MOUNT>.

- Koppel de huidige map als C:

`MOUNT C .`

- Koppel een specifieke map als C:

`MOUNT C {{C:\pad\naar\map}}`

- Koppel met een limiet voor vrije ruimte (in MB):

`MOUNT C {{C:\pad\naar\map}} -freesize {{1024}}`

- Koppel een floppystation:

`MOUNT A {{A:\}} -t floppy`

- Koppel een cd-romstation:

`MOUNT D {{D:\}} -t cdrom`

- Koppel een cd met extra opties:

`MOUNT D {{D:\}} -t cdrom -usecd {{0}} -ioctl`

- Ontkoppel een schijf:

`MOUNT -u {{C}}`
